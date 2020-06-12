from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    #path('', views.login, name='login'),
    path('login', views.login, name='login'),
    #path('signup', views.signup, name='signup'),
    path('patients', views.patients, name='patients'),
    #path('view_profile', views.view_profile, name='view_profile'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('locations', views.locations, name='locations'),
    path('doctor', views.doctor, name='doctor'),
    path('nurse', views.nurse, name='nurse'),
    path('ambulance', views.ambulance, name='ambulance'),
    path('add', views.add, name='add'),

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    #path('profile', views.profile, name='views.profile')

]


