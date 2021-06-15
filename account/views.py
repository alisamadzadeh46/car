from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('account:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('account:register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                    email=email,
                                                    password=password)
                    user.save()
                    messages.success(request, 'You are registered successfully. please login')
                    return redirect('account:login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('account:register')

    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('account:login')
    return render(request, 'account/login.html')


def dashboard(request):
    return render(request, 'account/dashboard.html')


def logout(request):
    return redirect('home:home')
