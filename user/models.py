from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='hesaplar/', blank=True)
    isim = models.CharField(max_length=100, null=True, blank=True)
    soyisim = models.CharField(max_length=100, null=True, blank=True)
    hakkinda = models.TextField(max_length=500, null=True, blank=True)
    websitesi = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Kullanıcı')
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to='profiller/')
    olusturulma_tarihi = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.isim