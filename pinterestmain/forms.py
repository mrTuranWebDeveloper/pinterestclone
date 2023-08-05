from django.forms import ModelForm
from .models import *

class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['title', 'description', 'image', 'url', 'board']
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'image': 'Görsel',
            'url': 'Bağlantı',
            'board': 'Pano'
        }
    def __init__(self, *args, **kwargs):
        super(PinForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class IdeaPinForm(ModelForm):
    class Meta:
        model = IdeaPin
        fields = ['title', 'description', 'image','url','board']
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'image': 'Görsel',
            'url': 'Bağlantı',
            'board': 'Pano'
        }
    def __init__(self,*args,**kwargs):
        super(IdeaPinForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})