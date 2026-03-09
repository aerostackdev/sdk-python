import asyncio
import json
import random
import re
import time
import uuid
import urllib.request
import urllib.parse
from typing import Any, Callable, Dict, List, Optional, Set
from .configuration import Configuration


class RealtimeSubscription:
    def __init__(self, client: 'Realtime', topic: str, filter: Optional[Dict[str, Any]] = None):
        self.client = client
        self.topic = topic
        self.filter = filter
        self._event_callbacks: Dict[str, Set[Callable[[Dict[str, Any]], None]]] = {}
        self.is_subscribed = False

    # ------------------------------------------------------------------
    # Backward-compatible property: return the union of all registered
    # callbacks regardless of event key.
    # ------------------------------------------------------------------
    @property
    def callbacks(self) -> Set[Callable[[Dict[str, Any]], None]]:
        out: Set[Callable[[Dict[str, Any]], None]] = set()
        for cbs in self._event_callbacks.values():
            out |= cbs
        return out

    def on(self, event: str, callback: Callable[[Dict[str, Any]], None]) -> 'RealtimeSubscription':
        """Register a callback for a specific event name.

        The *event* string is matched against ``payload["operation"]``
        (for db_change messages) **and** ``payload["event"]`` (for custom
        publish messages).  Use ``"*"`` to receive every message on this
        topic regardless of the event name.
        """
        if event not in self._event_callbacks:
            self._event_callbacks[event] = set()
        self._event_callbacks[event].add(callback)
        return self

    async def subscribe(self) -> 'RealtimeSubscription':
        if self.is_subscribed:
            return self
        await self.client._send({
            "type": "subscribe",
            "topic": self.topic,
            "filter": self.filter
        })
        self.is_subscribed = True
        return self

    async def unsubscribe(self):
        if not self.is_subscribed:
            return
        await self.client._send({
            "type": "unsubscribe",
            "topic": self.topic
        })
        self.is_subscribed = False
        self._event_callbacks.clear()

    async def publish(
        self,
        event: str,
        data: Any,
        persist: Optional[bool] = None,
        id: Optional[str] = None,
    ) -> None:
        """Publish a custom event to this subscription's topic.

        Sends a ``publish`` frame over the WebSocket connection.  The
        server will broadcast the event to all subscribers of the topic.

        :param event: Custom event name (e.g. ``"cursor_move"``).
        :param data: Arbitrary JSON-serialisable payload.
        :param persist: When ``True`` the server persists the event to
            history so it can be retrieved later via :meth:`get_history`.
        :param id: Optional client-generated message id (UUID recommended).
            If omitted the SDK generates one automatically.
        """
        msg: Dict[str, Any] = {
            "type": "publish",
            "topic": self.topic,
            "event": event,
            "data": data,
            "id": id or str(uuid.uuid4()),
        }
        if persist is not None:
            msg["persist"] = persist
        await self.client._send(msg)

    async def track(self, state: Dict[str, Any]) -> None:
        """Announce presence / track state on this topic.

        Sends a ``track`` frame so the server knows this client is
        present and associates the given ``state`` dict with the
        connection.

        :param state: Arbitrary JSON-serialisable presence state, e.g.
            ``{"user": "alice", "cursor": {"x": 10, "y": 20}}``.
        """
        await self.client._send({
            "type": "track",
            "topic": self.topic,
            "state": state,
        })

    async def untrack(self) -> None:
        """Remove presence / stop tracking state on this topic.

        Sends an ``untrack`` frame so the server removes this client
        from the presence set of the topic.
        """
        await self.client._send({
            "type": "untrack",
            "topic": self.topic,
        })

    async def get_history(
        self,
        limit: int = 50,
        before: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetch persisted event history for this topic via the HTTP API.

        Makes a GET request to the public realtime history endpoint.
        The API key from the client configuration is sent in the
        ``X-Aerostack-Key`` header.

        :param limit: Maximum number of events to return (default 50).
        :param before: Opaque cursor returned by a previous call; only
            events older than this cursor are returned.
        :returns: Parsed JSON response from the server.
        """
        return await self.client._get_history(
            topic=self.topic,
            limit=limit,
            before=before,
        )

    def _emit(self, payload: Dict[str, Any]):
        """Dispatch an incoming message to matching callbacks.

        A callback registered for event ``E`` fires when:
        - ``payload["event"] == E``, **or**
        - ``payload["operation"] == E``.

        Callbacks registered with the wildcard event ``"*"`` fire for
        every message on this topic.
        """
        # Determine which event keys this payload matches.
        matched_keys: Set[str] = set()
        event_name = payload.get("event")
        operation = payload.get("operation")
        if event_name:
            matched_keys.add(event_name)
        if operation:
            matched_keys.add(operation)

        # Gather the callbacks that should fire.
        targets: Set[Callable[[Dict[str, Any]], None]] = set()

        # Wildcard listeners always fire.
        if "*" in self._event_callbacks:
            targets |= self._event_callbacks["*"]

        for key in matched_keys:
            if key in self._event_callbacks:
                targets |= self._event_callbacks[key]

        # If no specific match and no wildcard, fall back to firing
        # ALL registered callbacks (preserves original behaviour where
        # .on("some_label", cb) would fire for every message).
        if not targets:
            for cbs in self._event_callbacks.values():
                targets |= cbs

        for cb in targets:
            try:
                cb(payload)
            except Exception as e:
                print(f"Realtime callback error: {e}")


class Realtime:
    _BASE_RECONNECT_MS = 1000
    _MAX_RECONNECT_MS = 30000

    def __init__(self, configuration: Configuration, max_reconnect_attempts: int = 0):
        self.configuration = configuration
        self.ws = None
        self.subscriptions: Dict[str, RealtimeSubscription] = {}
        self.is_connected = False
        self._listen_task: Optional[asyncio.Task] = None
        self._heartbeat_task: Optional[asyncio.Task] = None
        self._reconnect_attempts = 0
        self._send_queue: List[Dict[str, Any]] = []
        self._status = 'idle'
        self._status_listeners: set = set()
        self._last_pong: float = 0
        self._max_reconnect_attempts = max_reconnect_attempts if max_reconnect_attempts > 0 else float('inf')
        self._max_retries_listeners: set = set()

    @property
    def status(self) -> str:
        return self._status

    def on_status_change(self, cb) -> Callable:
        self._status_listeners.add(cb)
        return lambda: self._status_listeners.discard(cb)

    def on_max_retries_exceeded(self, cb) -> Callable:
        self._max_retries_listeners.add(cb)
        return lambda: self._max_retries_listeners.discard(cb)

    def _set_status(self, s: str):
        self._status = s
        for cb in self._status_listeners:
            try:
                cb(s)
            except Exception:
                pass

    def set_token(self, new_token: str):
        """Update auth token on a live connection (B4)."""
        asyncio.create_task(self._send({"type": "auth", "token": new_token}))

    def _get_api_key(self) -> str:
        """Extract the raw API key string from the configuration."""
        if self.configuration.api_key:
            return self.configuration.api_key.get("ApiKeyAuth", "")
        return ""

    def _get_http_base(self) -> str:
        """Derive the HTTP base URL (without ``/v1``) from the host."""
        host = self.configuration.host or "https://api.aerostack.dev/v1"
        return re.sub(r'/v1/?$', '', host)

    async def connect(self):
        if self.is_connected:
            return

        self._set_status('connecting')

        try:
            import websockets
        except ImportError:
            raise ImportError("websockets package required. Install with: pip install websockets")

        host = self.configuration.host or "https://api.aerostack.dev/v1"
        ws_base = re.sub(r'/v1/?$', '', host)
        ws_base = ws_base.replace('https://', 'wss://').replace('http://', 'ws://')
        
        api_key = self._get_api_key()

        ws_url = f"{ws_base}/api/realtime?apiKey={api_key}"

        self.ws = await websockets.connect(ws_url)
        self.is_connected = True
        self._reconnect_attempts = 0
        self._last_pong = time.time()
        self._set_status('connected')

        # Flush send queue
        while self._send_queue:
            msg = self._send_queue.pop(0)
            await self.ws.send(json.dumps(msg))

        self._listen_task = asyncio.create_task(self._listen())
        self._heartbeat_task = asyncio.create_task(self._heartbeat())

        # Re-subscribe
        for sub in self.subscriptions.values():
            await sub.subscribe()

    async def disconnect(self):
        self._set_status('disconnected')
        self.is_connected = False
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
            self._heartbeat_task = None
        if self.ws:
            await self.ws.close()
            self.ws = None
        if self._listen_task:
            self._listen_task.cancel()
            self._listen_task = None
        self._send_queue = []

    def channel(self, topic: str, filter: Optional[Dict[str, Any]] = None) -> RealtimeSubscription:
        if topic not in self.subscriptions:
            self.subscriptions[topic] = RealtimeSubscription(self, topic, filter)
        return self.subscriptions[topic]

    def send_chat(self, room_id: str, text: str):
        asyncio.create_task(self._send({"type": "chat", "roomId": room_id, "text": text}))

    async def _send(self, data: Dict[str, Any]):
        if self.ws and self.is_connected:
            await self.ws.send(json.dumps(data))
        else:
            self._send_queue.append(data)

    async def _get_history(
        self,
        topic: str,
        limit: int = 50,
        before: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Fetch event history for a topic from the HTTP API.

        Runs the blocking ``urllib`` call in the default executor so
        that the event loop is not blocked.
        """
        base = self._get_http_base()
        params: Dict[str, str] = {
            "room": topic,
            "limit": str(limit),
        }
        if before is not None:
            params["before"] = before

        url = f"{base}/api/v1/public/realtime/history?{urllib.parse.urlencode(params)}"
        api_key = self._get_api_key()

        def _do_request() -> Dict[str, Any]:
            req = urllib.request.Request(url, method="GET")
            req.add_header("X-Aerostack-Key", api_key)
            req.add_header("Accept", "application/json")
            with urllib.request.urlopen(req) as resp:
                body = resp.read().decode("utf-8")
                return json.loads(body)

        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, _do_request)

    async def _listen(self):
        try:
            async for message in self.ws:
                data = json.loads(message)
                msg_type = data.get("type")
                if msg_type == "pong":
                    self._last_pong = time.time()
                    continue
                if msg_type == "ack":
                    # Server acknowledgement — nothing to do.
                    continue
                if msg_type == "subscribed":
                    # Server confirmed subscription with its normalized topic
                    # (e.g. 'table/orders/<projectId>').
                    # Re-key our subscription map so incoming db_change
                    # messages can be routed correctly.
                    server_topic = data.get("topic", "")
                    for orig_topic in list(self.subscriptions.keys()):
                        if server_topic != orig_topic and server_topic.startswith(orig_topic):
                            sub = self.subscriptions.pop(orig_topic)
                            sub.topic = server_topic
                            self.subscriptions[server_topic] = sub
                            break
                    continue
                # Route messages to the matching subscription.
                # Supported inbound types: db_change, chat_message, event.
                topic = data.get("topic")
                if topic in self.subscriptions:
                    self.subscriptions[topic]._emit(data)
        except Exception as e:
            if self.is_connected:
                print(f"Realtime connection lost: {e}")
                self.is_connected = False
                self._set_status('reconnecting')
                if self._heartbeat_task:
                    self._heartbeat_task.cancel()
                    self._heartbeat_task = None
                # Check max retries
                if self._reconnect_attempts >= self._max_reconnect_attempts:
                    self._set_status('disconnected')
                    for cb in self._max_retries_listeners:
                        try:
                            cb()
                        except Exception:
                            pass
                    return
                delay_ms = min(
                    self._BASE_RECONNECT_MS * (2 ** self._reconnect_attempts),
                    self._MAX_RECONNECT_MS
                )
                jitter_ms = delay_ms * 0.3 * random.random()
                self._reconnect_attempts += 1
                await asyncio.sleep((delay_ms + jitter_ms) / 1000)
                await self.connect()

    async def _heartbeat(self):
        try:
            while self.is_connected:
                await asyncio.sleep(30)
                if self.is_connected:
                    await self._send({"type": "ping"})
                    # B3: Check for dead connection (no pong in 70s)
                    if self._last_pong > 0 and time.time() - self._last_pong > 70:
                        print("Realtime: no pong received, forcing reconnect")
                        if self.ws:
                            await self.ws.close()
        except asyncio.CancelledError:
            pass

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()


# Alias used by sdk.py
RealtimeClient = Realtime
