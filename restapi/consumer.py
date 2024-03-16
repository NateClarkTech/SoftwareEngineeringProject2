import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

"""
A Websocket for the chat signals
"""
class ChatConsumer(AsyncWebsocketConsumer):
    """
    Called when a client conects to the websocket
    """
    async def connect(self):
        self.room_group_name = "default_group"
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
    """
    Called when websocket closes to remove the client from the group
    """
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    """
    Called when a message is recived from the client(NOT USED)
    """
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.send(text_data=json.dumps({"message": message}))

    # Receive message from room group
    """
    Called to send signals to the client of DB changes
    """    
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))