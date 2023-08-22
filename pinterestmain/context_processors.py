from .models import *


from django.core.exceptions import ObjectDoesNotExist

def get_boards(request):
    try:
        recent_board = Board.objects.latest('created')
    except ObjectDoesNotExist:
        recent_board = None
    context = {
        'recent_board': recent_board


    }
    return context

    