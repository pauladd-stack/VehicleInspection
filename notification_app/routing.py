# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    #re_path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    #path('ws/<room_name>/', consumers.NotificationConsumer.as_asgi()),
    path('<room_name>/', consumers.NotifConsumer.as_asgi()),

]