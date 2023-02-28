
from django.urls import path, include

from chat_app import views

urlpatterns = [

    path('', views.rooms, name="rooms"),
    path('<slug:room_name>/', views.room, name='room'),
]