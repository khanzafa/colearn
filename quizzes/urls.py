from django.urls import path, include
from quizzes import views

app_name = 'quizzes'
urlpatterns = [
    path('kuis', views.KuisView.as_view(), name='kuis'),
    path('mata-kuliah/<int:course_id>/kuis', views.KuisLatihanView.as_view(), name='kuis-latihan'),
    path('mata-kuliah/<int:course_id>/kuis/<int:quiz_id>/detail', views.KuisDetailView.as_view(), name='kuis-detail'),
    path('mata-kuliah/kuis/hasil', views.KuisHasilView.as_view(), name='kuis-hasil')
]


