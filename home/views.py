from django.contrib import messages
from django.shortcuts import render, redirect
from cars.models import Cars
from .models import Team, Contact


def home(request):
    context = {
        'teams': Team.objects.all(),
        'featured_cars': Cars.objects.filter(is_featured=True).order_by('-created_data')[:6],
        'latest_cars': Cars.objects.order_by('-created_data')[:6],
        'model_search': Cars.objects.values_list('model', flat=True).distinct(),
        'city_search': Cars.objects.values_list('city', flat=True).distinct(),
        'year_search': Cars.objects.values_list('year', flat=True).distinct(),
        'body_style_search': Cars.objects.values_list('body_style', flat=True).distinct(),
        'total_cars': Cars.objects.count(),
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html', {'teams': Team.objects.all()})


def services(request):
    return render(request, 'home/services.html')


def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('home:contact')
    return render(request, 'home/contact.html')
