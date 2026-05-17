from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from cars.models import Message


def register(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('accounts:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('accounts:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('accounts:register')

        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password,
        )
        messages.success(request, 'Registration successful. Please login.')
        return redirect('accounts:login')

    return render(request, 'account/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('accounts:dashboard')
        messages.error(request, 'Invalid username or password.')
        return redirect('accounts:login')

    return render(request, 'account/login.html')


@login_required(login_url='accounts:login')
def dashboard(request):
    user_messages = Message.objects.filter(user_id=request.user.id).order_by('-create_data')
    return render(request, 'account/dashboard.html', {'messages_list': user_messages})


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home:home')
