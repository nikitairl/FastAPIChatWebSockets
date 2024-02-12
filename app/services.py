
import asyncio

from fastapi import WebSocket


class ConnectionManager:
    """
    Initialize the object with an empty
    list to store active WebSocket connections.
    """
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        try:
            self.active_connections.remove(websocket)
        except ValueError:
            pass

    async def send_personal_message(
        self,
        message: str,
        websocket: WebSocket
    ):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        # Use a list comprehension to collect coroutines for all sends
        send_coroutines = [
            connection.send_text(message)
            for connection in self.active_connections
        ]
        # Use asyncio.gather to send all messages concurrently
        await asyncio.gather(*send_coroutines)
