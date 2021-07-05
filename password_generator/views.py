from django.shortcuts import render
import pandas
import random

# Create your views here.
def generator(request):
    return render(request, 'generator/generator.html')

def password(request):

    password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()+_'))
    
    length = int(request.GET.get('length'))
    for i in range(length):
        password += random.choice(characters)
    
    return render(request, 'password/password.html', {'password' : password })

def save(request):
    
    if request.GET.get('name'):
        letter = request.GET.get('name')
        
    return render(request, 'password/password.html', {'code': letter})

