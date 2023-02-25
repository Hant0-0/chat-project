from django.urls import path

from chat_app.consumer import WSConsumer

ws_urlpatterns = [
    path('ws/room/', WSConsumer.as_asgi())
]