import asyncio
import json
import random
import math
import websockets
from typing import Any, Callable, Dict, Optional, Set
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
            cb(payload)

class Realtime(BaseSDK):
    _BASE_RECONNECT_MS = 1000
    _MAX_RECONNECT_MS = 30000

    def __init__(self, sdk_config, parent_ref=None):
        super().__init__(sdk_config, parent_ref=parent_ref)
        self.ws: Optional[websockets.WebSocketClientProtocol] = None
        self.subscriptions: Dict[str, RealtimeSubscription] = {}
        self.is_connected = False
        self._listen_task: Optional[asyncio.Task] = None
        self._reconnect_attempts = 0

    async def connect(self):
        if self.is_connected:
            return

        base_url = self.sdk_configuration.server_url.replace("http", "ws") + "/realtime"
        url = f"{base_url}?projectId={self.sdk_configuration.security.api_key_auth}"
        
        self.ws = await websockets.connect(url)
        self.is_connected = True
        self._reconnect_attempts = 0  # Reset on successful connection
        self._listen_task = asyncio.create_task(self._listen())
        
        # Re-subscribe
        for sub in self.subscriptions.values():
            await sub.subscribe()

    async def disconnect(self):
        self.is_connected = False
        if self.ws:
            await self.ws.close()
        if self._listen_task:
            self._listen_task.cancel()

    def channel(self, topic: str, filter: Optional[Dict[str, Any]] = None) -> RealtimeSubscription:
        if topic not in self.subscriptions:
            self.subscriptions[topic] = RealtimeSubscription(self, topic, filter)
        return self.subscriptions[topic]

    async def _send(self, data: Dict[str, Any]):
        if self.ws and self.is_connected:
            await self.ws.send(json.dumps(data))

    async def _listen(self):
        try:
            async for message in self.ws:
                data = json.loads(message)
                topic = data.get("topic")
                if topic in self.subscriptions:
                    self.subscriptions[topic]._emit(data)
        except Exception as e:
            if self.is_connected:
                print(f"Realtime connection lost: {e}")
                self.is_connected = False
                # Exponential backoff with jitter: 1s → 2s → 4s → ... → 30s
                delay_ms = min(
                    self._BASE_RECONNECT_MS * (2 ** self._reconnect_attempts),
                    self._MAX_RECONNECT_MS
                )
                jitter_ms = delay_ms * 0.3 * random.random()
                self._reconnect_attempts += 1
                await asyncio.sleep((delay_ms + jitter_ms) / 1000)
                await self.connect()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
