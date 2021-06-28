from django.shortcuts import render
from django.http import HttpResponse
from .models import project
# Create your views here.
def info(Requests):
    projects = project.objects.all()

    return render(Requests, 'portfolio/portifolio.html', {'projects' : projects})
