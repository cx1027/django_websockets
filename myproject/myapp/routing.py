from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/some_path/$', consumers.MyWebSocketConsumer.as_asgi()),
]
