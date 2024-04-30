from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()  # Case-insensitive comparison
            raw_password = form.cleaned_data.get('password1')

            if User.objects.filter(username__iexact=username).exists():
                messages.error(request, 'User with this username already exists')
                return redirect('login')

            user = form.save(commit=False)
            user.set_password(raw_password)
            user.save()

            messages.success(request, 'Sign up successful. Please log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

        
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('dashboard:index')
        return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have logged out')
    return redirect('login')

@login_required
def account(request):
    return render(request, 'users/account.html')

