import json

from channels.generic.websocket import AsyncWebsocketConsumer
from twisted.conch.ssh.connection import messages


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.group_room_name=f"chat_{self.room_name}"
        await self.channel_layer.group_add(
            self.group_room_name,
            self.channel_name,

            await self.connect(),
            await self.send(text_data=json.dumps({
                "message":f"room{self.room_name} connected"
            }))
        )
    async def disconnect(self, code_code):
        await self.channel_layer.group_discard(
            self.group_room_name,
            self.channel_name
        )


    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data["message"]

        await self.channel_layer.group_send({
            "type":"chat_message",
            "message":message

        }

        )
    async def chat_message(self,event):
        messages=event["message"]
        await self.send(text_data=json.dumps({
            "message":messages
        }))
