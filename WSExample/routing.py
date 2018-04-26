# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import app.routing
import app.consumers

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    ),

    'channel': ChannelNameRouter({
        'generate-id': app.consumers.GenerateConsumer,
    }),

})