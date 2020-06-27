from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    #path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('notification', views.notification, name='notification'),
    path('patients', views.patients, name='patients'),
    path('finddoctor', views.finddoctor, name='finddoctor'),
    path('chatting', views.chatting, name='chatting'),
    path('hospitals', views.hospitals, name='hospitals'),

    path('locations', views.locations, name='locations'),
    path('doctor', views.doctor, name='doctor'),
    path('nurse', views.nurse, name='nurse'),
    path('ambulance', views.ambulance, name='ambulance'),
    path('profile', views.profile, name='profile'),

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('files2links', views.files2links, name='views.files2links')

]


