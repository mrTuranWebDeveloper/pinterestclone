from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pin(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    image = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pins'
