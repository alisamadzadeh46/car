from django.contrib import messages
from django.shortcuts import render

from cars.models import Cars, Images
from .models import *


def home(request):
    teams = Team.objects.all()
    featured_cars = Cars.objects.order_by('-created_data').filter(is_featured=True)
    latest_cars = Cars.objects.order_by('-created_data')
    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,

    }
    return render(request, 'home/index.html', data)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        con = Contact(name=name, email=email, subject=subject, phone=phone, message=message)
        con.save()
        messages.success(request, 'Thank you')
    return render(request, 'home/contact.html')


def about(request):
    teams = Team.objects.all()
    return render(request, 'home/about.html', {'teams': teams})


def services(request):
    return render(request, 'home/services.html')
