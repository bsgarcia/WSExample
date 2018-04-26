# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer)
]

# from channels.routing import route
# from app.channel_client.consumers import ws_connect, ws_disconnect, ws_receive
# from app.channel_client.tasks import get_user_id
#
#
# channel_routing = [
#     route('websocket.connect', ws_connect),
#     route('websocket.disconnect', ws_disconnect),
#     route('websocket.receive', ws_receive),
#     route("get-user-id", get_user_id),
# ]
#
# websocket_urlpatterns = [
#     url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
# ]