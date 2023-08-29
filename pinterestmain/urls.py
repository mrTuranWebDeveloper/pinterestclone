from django.urls import path
from pinterestmain.views import *

urlpatterns = [
    path('', index, name='index'),
    path('pins/<int:pinId>', pinsDetail, name='pins'),
    path('ideapins/<int:ideapinId>', idea_pins_Detail, name='ideapins'),
    path('assign_pin_to_board/<str:pin_type>/<int:pinId>/<int:ideapinId>/<int:board_id>/', assign_pin_to_board, name='assign_pin_to_board'),
    path('create_comment/<int:content_type_id>/<int:object_id>/', create_comment, name='create_comment'),
    path('upvotes/', create_upvote, name='create_upvote'),
    path('create_pin/', create_pin, name='create_pin'),
    path('create_ideapin/', create_idea_pin, name='create_idea_pin'),
    path('homepage/', homepage, name='homepage'),
    path('about/', about_page, name='about'),
    path('business/', business_page, name='business'),
    path('blog/', blog_page, name='blog'),
    path('settings/', settings_page, name='settings'),
    path('profile/', profile_page, name='profile')
]