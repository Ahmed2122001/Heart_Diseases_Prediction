from django.urls import path
from . import views


urlpatterns=[
    path('signUp', views.signUp, name='signUp'),
    path('Login', views.Login, name='Login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout')
]