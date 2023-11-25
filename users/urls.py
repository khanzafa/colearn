from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views
from users.views import dashboard

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name='register'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
]