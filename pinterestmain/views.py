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
    return render(request, 'detail.html', context)

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
    context = {
        'pins':pins
    }
    return render(request, 'homepage.html', context)