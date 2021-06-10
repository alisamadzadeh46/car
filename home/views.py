from django.shortcuts import render

from cars.models import Cars, Images
from .models import *


def home(request):
    teams = Team.objects.all()
    featured_cars = Cars.objects.order_by('-created_data').filter(is_featured=True)
    return render(request, 'home/index.html', {'teams': teams, 'featured_cars': featured_cars})


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
