from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)


        # this is to check if the username exists then tell the user to pick a different one
        if user.exists():
            messages.info(request, "Username aleady exists.")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)  # this is to encrypt the password
        user.save()
        messages.info(request, "account created successfully.")
        return redirect('/login/')




    return render(request, "registration.html")