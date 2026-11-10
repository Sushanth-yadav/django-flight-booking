from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name = 'login_'),
    path('register/',register,name = 'register'),
    path('profile/',profile,name='profile'),
    path('logout_/',logout_,name='logout_'),
    path('update/',update,name='update'),
    path('fpasw/',fpasw,name='fpasw')
]