from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse
from users.forms import CustomUserCreationForm
from django.urls import reverse

def register(request):

    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'users/dashboard.html')
        else:
            return render(
                request, "registration/register.html",
                {"form": form}
            )


def dashboard(request):
    if request.method == 'GET':
        return render(request, 'users/dashboard.html')

    