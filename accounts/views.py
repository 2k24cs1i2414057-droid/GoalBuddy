from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from goal.models import Student


# def login(request):
#     return render(request, "accounts/login.html")


# def signup(request):
#     return render(request, "accounts/signup.html")



def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        # User + Student create karo
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        Student.objects.create(user=user, phone=phone)

        messages.success(request, 'Account created! Please login.')
        return redirect('login')

    return render(request, 'accounts/signup.html')


def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')