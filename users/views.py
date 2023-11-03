from django.shortcuts import render, redirect
# from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect ke halaman setelah pendaftaran berhasil
            # return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def dashboard(request):
    return render(request, 'users/dashboard.html')

# def login(request):
    # return auth_views.LoginView.as_view(template_name='login.html')

# def login_view(request):
#     if request.method == 'POST':
#         # Proses form login
#         # ...
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Selamat datang, ' + user.username + '!')
#             return redirect('profile')  # atau sesuaikan dengan halaman tujuan

# @login_required
# def profile(request):
#     return render(request, 'profile.html')