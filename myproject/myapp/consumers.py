from channels.generic.websocket import AsyncWebsocketConsumer
import json

# class MyWebSocketConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         # Additional connection logic here

#     async def disconnect(self, close_code):
#         # Handle disconnection logic here
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         # Handle received data here
#         await self.send(text_data=json.dumps({
#             'message': 'Response from server'
#         }))

# myapp/consumers.py
from .tasks import transcribe_audio

class MyWebSocketConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data):
        data = json.loads(text_data)
        audio_file_path = data['audio_file_path']  # Assume you get the audio file path

        # Call the Celery task
        transcribe_audio.delay(audio_file_path)  # This will queue the task

        await self.send(text_data=json.dumps({
            'message': 'Transcription started'
        }))
