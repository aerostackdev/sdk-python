import asyncio
import json
import random
import re
import time
from typing import Any, Callable, Dict, List, Optional, Set
from .basesdk import BaseSDK


class RealtimeSubscription:
    def __init__(self, client: 'Realtime', topic: str, filter: Optional[Dict[str, Any]] = None):
        self.client = client
        self.topic = topic
        self.filter = filter
        self.callbacks: Set[Callable[[Dict[str, Any]], None]] = set()
        self.is_subscribed = False

    def on(self, event: str, callback: Callable[[Dict[str, Any]], None]) -> 'RealtimeSubscription':
        self.callbacks.add(callback)
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
        self.callbacks.clear()

    def _emit(self, payload: Dict[str, Any]):
        for cb in self.callbacks:
            try:
                cb(payload)
            except Exception as e:
                print(f"Realtime callback error: {e}")


class Realtime(BaseSDK):
    _BASE_RECONNECT_MS = 1000
    _MAX_RECONNECT_MS = 30000

    def __init__(self, sdk_config, parent_ref=None, max_reconnect_attempts: int = 0):
        super().__init__(sdk_config, parent_ref=parent_ref)
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

    async def connect(self):
        if self.is_connected:
            return

        self._set_status('connecting')

        try:
            import websockets
        except ImportError:
            raise ImportError("websockets package required. Install with: pip install websockets")

        ws_base = re.sub(r'/v1/?$', '', self.sdk_configuration.server_url or '')
        ws_base = ws_base.replace('https://', 'wss://').replace('http://', 'ws://')
        sec = self.sdk_configuration.security
        if callable(sec):
            sec = sec()
        api_key = (getattr(sec, 'api_key_auth', '') or '') if sec else ''
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

    async def _listen(self):
        try:
            async for message in self.ws:
                data = json.loads(message)
                msg_type = data.get("type")
                if msg_type == "pong":
                    self._last_pong = time.time()
                    continue
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
