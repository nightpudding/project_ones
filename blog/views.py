from django.shortcuts import render
from django.http import HttpResponse
from .models import blog

# Create your views here.
def all_blogs(Requests):
    blogs = blog.objects.all()
    return render(Requests, 'blog/all_blog.html', {'blogs':blogs})
