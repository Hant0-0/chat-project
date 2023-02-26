from django.shortcuts import render

def chat(request):
    return render(request, 'chat_app/chat.html')


def room(request, room_name):
    return render(request, 'chat_app/room.html', {'room_name': room_name})

