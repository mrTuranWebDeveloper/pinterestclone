from django.urls import path
from pinterestmain.views import *

urlpatterns = [
    path('', index, name='index')
]