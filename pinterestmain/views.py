from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def pinsDetail(request,pinId):
    pins = Pin.objects.get(id=pinId)
    content_type = ContentType.objects.get_for_model(Pin)
    comments = Comment.objects.filter(content_type=content_type, object_id=pins.id)
    context = {
        'pins':pins,
        'content_type':content_type,
        'comments':comments
    }
    return render(request, 'pins.html', context)

def idea_pins_Detail(request,ideapinId):
    ideapins = IdeaPin.objects.get(id=ideapinId)
    content_type = ContentType.objects.get_for_model(IdeaPin)
    comments = Comment.objects.filter(content_type=content_type, object_id=ideapins.id)
    context = {
        'ideapins':ideapins,
        'content_type':content_type,
        'comments':comments
    }
    return render(request, 'ideapins.html', context)

def create_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            form.save()
            return redirect('index')  # Daha sonra homepage olarak değiştirilecek
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
            form.save()
            return redirect('index')
    else:
        form = IdeaPinForm()
    context = {
        'form':form
    }
    return render(request, 'create_ideapin.html', context)

def homepage(request):
    pins = Pin.objects.all()
    ideapins = IdeaPin.objects.all()
    context = {
        'pins':pins,
        'ideapins':ideapins
    }
    return render(request, 'homepage.html', context)

def about_page(request):
    return render(request, 'about.html')

def business_page(request):
    return render(request, 'business.html')

def blog_page(request):
    return render(request, 'blog.html')


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