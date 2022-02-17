from django.shortcuts import render
from django.http import HttpResponse
from .models import blog

# Create your views here.
def all_blogs(Requests):
    numbers = 0
    for i in range(0,100,5):
        numbers = i
        length = len(blog.objects.all()) - numbers
        if length >= numbers+5:
            blogs = blog.objects.order_by('-datetime')[numbers:numbers+5]
        else : 
            blogs = blog.objects.order_by('-date')[numbers:len(blog.objects.all())]
        return render(Requests, 'blog/all_blog.html', {'blogs':blogs})
