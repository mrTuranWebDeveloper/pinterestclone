from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pin(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='pins/')
    url = models.URLField()
    board = models.ForeignKey('Board', on_delete=models.CASCADE,  related_name='pins', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pins'

class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=True, null=True)
    board_pins = models.ManyToManyField(Pin, related_name='boards')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    group_members = models.ManyToManyField(User,  related_name='groups_joined')
    group_boards = models.ManyToManyField(Board)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'