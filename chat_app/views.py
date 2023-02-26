from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'chat_app/home.html')

def chat(request):
    return render(request, 'chat_app/chat.html')


def room(request, room_name):
    return render(request, 'chat_app/room.html', {'room_name': room_name})

def signupuser(requset):
    if requset.method == 'GET':
        return render(requset, 'chat_app/signup.html', {'form': UserCreationForm()})
    else:
        if requset.POST['password1'] == requset.POST['password2']:
            user = User.objects.create_user(username=requset.POST['username'], password=requset.POST['password1'])
            user.save()
            login(requset, user)
            return redirect('home')

def signinuser(request):
    if request.method == 'GET':
        return render(request, 'chat_app/signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        user.save()
        login(request, user)
        return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        redirect('home')




