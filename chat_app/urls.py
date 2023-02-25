
from django.urls import path, include

from chat_app import views

urlpatterns = [

    path('chat/', views.chat, name='chat'),
    path('chat/room/', views.room, name='room')
]