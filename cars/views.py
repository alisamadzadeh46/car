from django.shortcuts import render

def cars(request):
    return render(request,'home/cars.html')
