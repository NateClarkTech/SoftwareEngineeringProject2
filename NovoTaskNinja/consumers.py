import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message  # Adjust the import according to your app structure and model location
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Save the message to the database
        await self.save_message(username, message)

        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "chat_message",
                "message": message,
                "username": username,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
        }))

    @database_sync_to_async
    def save_message(self, username, message):
        user = User.objects.get(username=username)  # Assuming the username uniquely identifies a user
        Message.objects.create(user=user, message=message)
