from channels.generic.websocket import WebsocketConsumer, SyncConsumer, AsyncConsumer
from asgiref.sync import async_to_sync, sync_to_async

import asyncio

import json
import time
import numpy as np


class Consumer(WebsocketConsumer):

    group_test = 'test'

    def connect(self):

        async_to_sync(self.channel_layer.group_add)(
            self.group_test,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_test,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):


        async_to_sync(self.channel_layer.send)(
            'generate-id',
            {
                "type": "generate.id",
                "message": "tamere"
            }
        )

    def group_message(self, message):

        self.send(text_data=message["message"])


class GenerateConsumer(AsyncConsumer):

    async def generate_id(self, message):

        time.sleep(3)

        await self.channel_layer.group_send(
            'test',
            {
                'type': 'group.message',
                'message': message['message']
            }

        )




