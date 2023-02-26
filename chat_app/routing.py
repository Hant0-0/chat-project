from django.urls import path, re_path

from chat_app.consumer import WSConsumer

ws_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', WSConsumer.as_asgi()),
]