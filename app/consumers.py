import json
import time
import numpy as np

from channels.generic.websocket import WebsocketConsumer, AsyncConsumer
from asgiref.sync import async_to_sync


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

        print('text data: ', text_data)
        print('bytes data: ', bytes_data)
        async_to_sync(self.channel_layer.send)(
            'generate-id',
            {
                'type': 'generate.id',
            }
        )

        self.send(text_data='ok')

    def group_message(self, message):

        self.send(text_data=message['message'])


class GenerateConsumer(AsyncConsumer):

    async def generate_id(self, *args):

        time.sleep(2)

        await self.channel_layer.group_send(
            'test',
            {
                'type': 'group.message',
                'message': str(np.random.randint(999999999))
            }

        )


