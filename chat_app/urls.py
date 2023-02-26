
from django.urls import path, include

from chat_app import views

urlpatterns = [

    path('', views.chat, name='chat'),
    path('<str:room_name>/', views.room, name='room')
]