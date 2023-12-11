from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views
# from users.views import dashboard

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name='register')
]