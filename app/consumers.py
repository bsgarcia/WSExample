import time
import numpy as np

from channels.generic.websocket import WebsocketConsumer, SyncConsumer
from asgiref.sync import async_to_sync


from channels.layers import get_channel_layer

import app.views


class WebSocketConsumer(WebsocketConsumer):

    group_test = 'test'

    def connect(self):

        async_to_sync(self.channel_layer.group_add)(
            self.group_test,
            self.channel_name
        )

        self.accept()

        self.send(text_data='ok')

    def disconnect(self, close_code):

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_test,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):

        print('About to send from ext')
        app.views.ext_f()
        print('done')

    def group_message(self, message):

        self.send(text_data=message['text'])


def f(x):
    return x**2


class MainConsumer(SyncConsumer):

    def generate_id(self, *args):

        time.sleep(2)

        async_to_sync(self.channel_layer.group_send)(
            'test',
            {
                'type': 'group.message',
                'message': str(np.random.randint(999999999))
            }

        )


class WSDialog:

    @staticmethod
    def group_send(group, data):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'test',
            {
                'type': 'group.message',
                'text': data['message']
            }
        )
