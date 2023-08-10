from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Pin(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='pins/')
    url = models.URLField(null=True, blank=True)
    board = models.ForeignKey('Board', on_delete=models.CASCADE,  related_name='pins', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pins'

class IdeaPin(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='ideapins/')
    url = models.URLField(null=True, blank=True)
    board = models.ForeignKey('Board', on_delete=models.CASCADE, related_name='ideapins', null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='ideapins', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ideapins'


class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='boards/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True)
    board_pins = models.ManyToManyField(Pin, related_name='boards')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='groups/', null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    group_members = models.ManyToManyField(User,  related_name='groups_joined')
    group_boards = models.ManyToManyField(Board, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]
