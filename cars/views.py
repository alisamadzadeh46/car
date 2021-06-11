from django.shortcuts import render

from .models import Cars


def cars(request):
    return render(request, 'cars/cars.html')


def car_detail(request, id):
    # car = Cars.objects.filter(cars)
    return render(request, 'cars/detail.html')
