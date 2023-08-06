from django.urls import path
from pinterestmain.views import *

urlpatterns = [
    path('', index, name='index'),
    path('pins/<int:pinId>', pinsDetail, name='pins'),
    path('create_pin/', create_pin, name='create_pin'),
    path('create_ideapin/', create_idea_pin, name='create_idea_pin'),
    path('homepage/', homepage, name='homepage'),
    path('about/', about_page, name='about'),
    path('business/', business_page, name='business'),
    path('blog/', blog_page, name='blog'),
]