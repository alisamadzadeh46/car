from django.shortcuts import render, redirect


def register(request):
    return render(request, 'account/register.html')


def login(request):
    return render(request, 'account/login.html')


def dashboard(request):
    return render(request, 'account/dashboard.html')


def logout(request):
    return redirect('home:home')
