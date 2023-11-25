from django.urls import path, include
from courses import views

urlpatterns = [
    path('mata-kuliah', views.matkul, name='tugas'),
    path('mata-kuliah/detail', views.detailMatkul, name='detail')

]