from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
]
