from django.shortcuts import render, get_object_or_404

from .models import Cars, Images


def cars(request):
    return render(request, 'cars/cars.html')


def car_detail(request, id):
    car = get_object_or_404(Cars, pk=id)
    images = Images.objects.filter(cars_id=id)
    data = {
        'car': car,
        'images': images,
    }
    return render(request, 'cars/detail.html', data)
