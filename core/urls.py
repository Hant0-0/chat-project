from django.contrib import admin
from django.urls import path, include
from chat_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rooms/', include('chat_app.urls')),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('signin/', views.signinuser, name='signinuser'),
    path('logout/', views.logoutuser, name='logoutuser')
]
