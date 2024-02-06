from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from dashboard.views import dashboard_view

# Create your views here.

# logining/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def logining(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User exists, check password
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')  # Use the correct URL name for redirection
        else:
            # User does not exist or password is incorrect
            messages.error(request, 'Invalid username or password.')
            return redirect('logining')  # Redirect back to the login page

    return render(request, "logining.html")

def logout_page(request):
    logout(request)
    return redirect('landing_page')