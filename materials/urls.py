from django.urls import path, include
from materials import views

urlpatterns = [
    path('mata-kuliah/materi', views.materi, name='materi'),
    path('mata-kuliah/materi/detail', views.detailMateri, name='detail')
    
]