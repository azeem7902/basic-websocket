from django.urls import  re_path
from myapp import consumers
websocket_url_patterns=[
    re_path(r"ws/p?<room_name>\w+)/$",consumers)
]