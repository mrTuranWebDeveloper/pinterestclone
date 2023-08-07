from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def pinsDetail(request,pinId):
    pins = Pin.objects.get(id=pinId)
    context = {
        'pins':pins
    }
    return render(request, 'pins.html', context)

def idea_pins_Detail(request,ideapinId):
    ideapins = IdeaPin.objects.get(id=ideapinId)
    context = {
        'ideapins':ideapins
    }
    return render(request, 'ideapins.html', context)

def create_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
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
        form = IdeaPinForm(request.Post, request.FILES)
        if form.is_valid():
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
