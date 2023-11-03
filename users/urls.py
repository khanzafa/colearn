from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('profile/', views.profile, name='profile'),
]