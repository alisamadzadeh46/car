from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'test')
    return render(request, 'account/register.html')


def login(request):
    return render(request, 'account/login.html')


def dashboard(request):
    return render(request, 'account/dashboard.html')


def logout(request):
    return redirect('home:home')
