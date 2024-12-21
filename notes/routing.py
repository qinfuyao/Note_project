from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notes/(?P<room_name>\w+)/$', consumers.NotesConsumer.as_asgi()),
]