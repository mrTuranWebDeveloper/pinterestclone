from django.urls import path
from pinterestmain.views import *

urlpatterns = [
    path('', index, name='index'),
    path('pins/', pinsDetail, name='pins'),
    path('create_pin/', create_pin, name='create_pin')
]