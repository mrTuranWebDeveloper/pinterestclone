from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pin)
admin.site.register(IdeaPin)
admin.site.register(Board)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Upvote)