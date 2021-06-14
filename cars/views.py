from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Cars, Images


def cars(request):
    car = Cars.objects.order_by('-created_data')
    #  Just change the number 2 to the desired number
    paginator = Paginator(car, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'car': paged_cars,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    car = get_object_or_404(Cars, pk=id)
    images = Images.objects.filter(cars_id=id)
    data = {
        'car': car,
        'images': images,
    }
    return render(request, 'cars/detail.html', data)


def search(request):
    car = Cars.objects.order_by('-created_data')
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            car = car.filter(car_name__icontains=q)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            car = car.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            car = car.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            car = car.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            car = car.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            car = car.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'car': car,
    }
    return render(request, 'cars/search.html', data)
