from django.urls import path, include
from tasks import views

urlpatterns = [
    path('mata-kuliah/tugas', views.tugas, name='tugas'),
    path('mata-kuliah/tugas/detail', views.detailTugas, name='detail'),
]