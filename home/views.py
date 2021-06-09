from django.shortcuts import render
from .models import *


def home(request):
    teams = Team.objects.all()
    return render(request, 'home/index.html', {'teams': teams})


def contact(request):
    return render(request, 'home/contact.html')


def login(request):
    return render(request, 'home/login.html')


def register(request):
    return render(request, 'home/register.html')


def about(request):
    teams = Team.objects.all()
    return render(request, 'home/about.html', {'teams': teams})


def services(request):
    return render(request, 'home/services.html')
