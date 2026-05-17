from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cars, Images, Message


def cars(request):
    car_list = Cars.objects.order_by('-created_data')
    paginator = Paginator(car_list, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    context = {
        'car': paged_cars,
        'model_search': Cars.objects.values_list('model', flat=True).distinct(),
        'city_search': Cars.objects.values_list('city', flat=True).distinct(),
        'year_search': Cars.objects.values_list('year', flat=True).distinct(),
        'body_style_search': Cars.objects.values_list('body_style', flat=True).distinct(),
        'total_cars': car_list.count(),
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, id):
    car = get_object_or_404(Cars, pk=id)
    images = Images.objects.filter(cars_id=id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You need to login to send an inquiry.')
            return redirect('accounts:login')

        if Message.objects.filter(car_id=id, user_id=request.user.id).exists():
            messages.error(request, 'You have already sent an inquiry for this car.')
            return redirect('cars:car_detail', id=id)

        Message.objects.create(
            car=car,
            car_name=request.POST.get('car_name', car.car_name),
            user=request.user,
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            customer_need=request.POST['customer_need'],
            city=request.POST['city'],
            state=request.POST['state'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        messages.success(request, 'Your inquiry has been submitted. We will get back to you shortly.')
        return redirect('cars:car_detail', id=id)

    context = {
        'car': car,
        'images': images,
        'related_cars': Cars.objects.filter(model=car.model).exclude(pk=id)[:3],
    }
    return render(request, 'cars/detail.html', context)


def search(request):
    car = Cars.objects.order_by('-created_data')

    filters = {
        'q': ('car_name__icontains', request.GET.get('q')),
        'model': ('model__iexact', request.GET.get('model')),
        'city': ('city__iexact', request.GET.get('city')),
        'year': ('year__iexact', request.GET.get('year')),
        'body_style': ('body_style__iexact', request.GET.get('body_style')),
        'transmission': ('transmission__iexact', request.GET.get('transmission')),
    }

    for key, (lookup, value) in filters.items():
        if value:
            car = car.filter(**{lookup: value})

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        car = car.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'car': car,
        'result_count': car.count(),
        'model_search': Cars.objects.values_list('model', flat=True).distinct(),
        'city_search': Cars.objects.values_list('city', flat=True).distinct(),
        'year_search': Cars.objects.values_list('year', flat=True).distinct(),
        'body_style_search': Cars.objects.values_list('body_style', flat=True).distinct(),
        'transmission_search': Cars.objects.values_list('transmission', flat=True).distinct(),
    }
    return render(request, 'cars/search.html', context)
