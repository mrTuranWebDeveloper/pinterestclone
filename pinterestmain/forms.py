from django.forms import ModelForm
from .models import *

class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'image': 'Görsel'
        }