import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import notification_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vehicle_website.settings')


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            #chat_app.routing.websocket_urlpatterns
          notification_app.routing.websocket_urlpatterns
        )
    ),
})