from .models import *

def get_boards(request):
    recent_board = Board.objects.latest('created')
    context = {
        'recent_board': recent_board
    }
    return context