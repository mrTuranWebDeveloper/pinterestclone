from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def pinsDetail(request,pinId):
    pins = Pin.objects.get(id=pinId)
    content_type = ContentType.objects.get_for_model(Pin)
    comments = Comment.objects.filter(content_type=content_type, object_id=pins.id)
    user = request.user
    count = Comment.objects.filter(object_id=pins.id, is_deleted=False).count()
    recent_board_pin = Board.objects.filter(board_pins__id=pinId).order_by('-id').first()
    boards = Board.objects.all()
    context = {
        'pins':pins,
        'content_type':content_type,
        'comments':comments,
        'count':count,
        'boards':boards,
        'pin_type': 'pin',
        'pin_id': pinId,
        'recent_board_pin': recent_board_pin
    }
    return render(request, 'pins.html', context)

def idea_pins_Detail(request,ideapinId):
    ideapins = IdeaPin.objects.get(id=ideapinId)
    content_type = ContentType.objects.get_for_model(IdeaPin)
    comments = Comment.objects.filter(content_type=content_type, object_id=ideapins.id)
    user = request.user
    count = Comment.objects.filter(object_id=ideapins.id, is_deleted=False).count()
    recent_board_ideapin = Board.objects.filter(board_idea_pins__id=ideapinId).order_by('-id').first()
    boards = Board.objects.all()
    context = {
        'ideapins':ideapins,
        'content_type':content_type,
        'comments':comments,
        'count': count,
        'boards': boards,
        'pin_type': 'ideapin',
        'ideapin_id': ideapinId,
        'recent_board_ideapin':recent_board_ideapin
    }
    return render(request, 'ideapins.html', context)

def homepage(request):
    pins = Pin.objects.all()
    ideapins = IdeaPin.objects.all()
    boards = Board.objects.all()
    context = {
        'pins':pins,
        'ideapins':ideapins,
        'boards':boards
    }
    return render(request, 'homepage.html', context)

def about_page(request):
    return render(request, 'about.html')

def business_page(request):
    return render(request, 'business.html')

def blog_page(request):
    return render(request, 'blog.html')

def settings_page(request):
    return render(request, 'settings.html')

def create_comment(request, content_type_id, object_id):
    content_type = ContentType.objects.get_for_id(content_type_id)
    obj = content_type.get_object_for_this_type(id=object_id)

    if request.method == 'POST':
        content = request.POST['content']
        if len(content) > 500:
            messages.error(request, 'Comment cannot be longer than 500 characters.')
            if content_type.model == 'pin':
                return redirect('pins', pinId=object_id)
            elif content_type.model == 'ideapin':
                return redirect('ideapins', ideapinId=object_id)
        commenter = request.user

        comment = Comment(content=content, commenter=commenter, content_object=obj)
        comment.save()

        if content_type.model == 'pin':
            return redirect('pins', pinId=object_id)
        elif content_type.model == 'ideapin':
            return redirect('ideapins', ideapinId=object_id)
    else:
        context = {
            'object_id': object_id,
            'obj': obj
        }
        return render(request, context)
    
@login_required

def create_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            board = form.cleaned_data['board']
            board.board_pins.add(pin)
            board.save()
            return redirect('homepage') 
    else:
        form = PinForm()
    context = {
        'form':form
    }

    return render(request, 'create_pin.html', context)

def create_idea_pin(request):
    if request.method == 'POST':
        form = IdeaPinForm(request.POST, request.FILES)
        if form.is_valid():
            ideapin = form.save(commit=False)
            ideapin.user = request.user
            ideapin.save()
            board = form.cleaned_data['board']
            board.board_idea_pins.add(ideapin)
            board.save()
            return redirect('homepage')
    else:
        form = IdeaPinForm()
    context = {
        'form':form
    }
    return render(request, 'create_ideapin.html', context)

def assign_pin_to_board(request, pin_type, pinId, ideapinId, board_id):
    if pin_type == 'pin':
        pin = get_object_or_404(Pin, pk=pinId)
        board = get_object_or_404(Board, pk=board_id)
        board.board_pins.add(pin)
        return redirect('pins', pinId=pinId)
    elif pin_type == 'ideapin':
        ideapin = get_object_or_404(IdeaPin, pk=ideapinId)
        board = get_object_or_404(Board, pk=board_id)
        board.board_idea_pins.add(ideapin)
        return redirect('ideapins', ideapinId=ideapinId)