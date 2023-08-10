from django.urls import path
from user.views import *

urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login')
]