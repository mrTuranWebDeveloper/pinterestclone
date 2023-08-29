from .models import *

def get_profiles(request):
    profiller = Profile.objects.filter(user = request.user) if request.user.is_authenticated else ''
    context = {
        'profiller':profiller
    }
    return context

def get_hesap(request):
    hesapBilgi = Hesap.objects.filter(user = request.user) if request.user.is_authenticated else ''
    context = {
        'hesapBilgi' : hesapBilgi,
    }
    return context