from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Additional connection logic here

    async def disconnect(self, close_code):
        # Handle disconnection logic here
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle received data here
        await self.send(text_data=json.dumps({
            'message': 'Response from server'
        }))
