from .consumers import chatConsumer
from django.urls import re_path


ws_urls = [
    re_path(r'ws/message/(?P<room_name>\w+)/$', chatConsumer.as_asgi())
]