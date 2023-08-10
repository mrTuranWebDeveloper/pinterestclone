from .models import *

def get_profiles(request):
    profiller = Profile.objects.filter(user = request.user) if request.user.is_authenticated else ''
    context = {
        'profiller':profiller
    }
    return context