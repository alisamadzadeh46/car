from django.shortcuts import render
from .models import *


def home(request):
    teams = Team.objects.all()
    return render(request, 'home/index.html', {'teams': teams})
