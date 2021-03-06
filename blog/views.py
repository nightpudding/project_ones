from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import blog

# Create your views here.
def all_blogs(Requests):
    blogs_count = blog.objects.count()
    blogs = blog.objects.order_by('-date')[:1]
    return render(Requests, 'blog/all_blog.html', {'blogs':blogs, 'blogs_count':blogs_count})

def detail(request, blog_id):
    Blog = get_object_or_404( blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':Blog})
