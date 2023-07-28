from django.urls import path
from pinterestmain.views import *

urlpatterns = [
    path('', index, name='index'),
    path('pins/', pinsDetail, name='pins')
]