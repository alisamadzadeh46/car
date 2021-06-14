from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Cars, Images


def cars(request):
    car = Cars.objects.order_by('-created_data')
    #  Just change the number 2 to the desired number
    paginator = Paginator(car, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
    data = {
        'car': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
    model_search = Cars.objects.values_list('model', flat=True).distinct()
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Cars.objects.values_list('transmission', flat=True).distinct()
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

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            car = car.filter(transmission__iexact=transmission)

    data = {
        'car': car,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)
