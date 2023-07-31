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
    def __init__(self, *args, **kwargs):
        super(PinForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})