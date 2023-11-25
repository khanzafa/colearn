from django.urls import path, include
from quizzes import views

urlpatterns = [
    path('kuis', views.kuis, name='kuis'),
    path('mata-kuliah/kuis-latihan', views.kuisLatihan, name='kuis'),
    path('mata-kuliah/kuis-latihan/detail', views.detailKuisLatihan, name='detail'),
    path('mata-kuliah/kuis-latihan/hasil', views.hasilKuisLatihan, name='hasil')
]