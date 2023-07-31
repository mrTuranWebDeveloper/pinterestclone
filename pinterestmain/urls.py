from django.urls import path
from pinterestmain.views import *

urlpatterns = [
    path('', index, name='index'),
    path('pins/<int:pinId>', pinsDetail, name='pins'),
    path('create_pin/', create_pin, name='create_pin')
]