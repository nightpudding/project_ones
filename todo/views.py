from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from .models import basic

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        #註冊頁面
        print(str(request))
        return render(request,'todowoo/signup_page.html', {'form':UserCreationForm()})
    
    elif request.method == 'POST':
        #註冊驗證
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                print(str(request))
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todowoo/signup_page.html', {'form':UserCreationForm(), 'error':'用戶名已被使用'})
        else:
            return render(request,'todowoo/signup_page.html', {'form':UserCreationForm(), 'error':'密碼不相符'})

def currenttodos(request):
    #登入後畫面
    return render(request, 'todowoo/currenttodos.html')

def logoutuser(request):
    #登出
    if request.method == 'POST':
        logout(request)
    return redirect('home')
    
def loginuser(request):
    #登入
    if request.method == 'GET':
        print(str(request))
        return render(request,'todowoo/signup_page.html', {'form':AuthenticationForm()})
    elif request.method == 'POST':
        #create a new user
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                print(str(request))
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todowoo/signup_page.html', {'form':AuthenticationForm(), 'error':'用戶名已被使用'})
        else:
            
            return render(request,'todowoo/signup_page.html', {'form':AuthenticationForm(), 'error':'密碼不相符'})

        
    

        