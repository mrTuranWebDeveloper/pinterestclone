from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST.get('email')
        resim = request.FILES['resim']
        sifre = request.POST['sifre']
        sifre2 = request.POST['sifre2']

        if sifre == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request, 'Kullanıcı adı zaten mevcut!')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email kullanımda!')
            elif len(sifre) < 6:
                messages.error(request, 'Şifre en az 6 karakter olmalıdır!')
            elif kullanici.lower() in sifre.lower():
                messages.error(request, 'Kullanıcı adı ile şifre benzer olmamalıdır!')
            else:
                # kullanıcı kayıt işlemi
                user = User.objects.create_user(
                    username = kullanici,
                    email = email,
                    password = sifre
                )
                Hesap.objects.create(
                    user = user,
                    resim = resim
                )
                user.save()
                messages.success(request, 'Kayıt tamamlandı. Giriş yapabilirsiniz')
                return redirect('index')
        else:
            messages.error(request, 'Şifreler eşleşmedi!')
    return render(request, 'register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yapıldı.')
            return redirect('homepage')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
            return redirect('login')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('index')