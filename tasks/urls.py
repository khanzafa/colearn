from django.urls import path, include
from tasks import views

app_name = 'tasks'
urlpatterns = [
    path('mata-kuliah/<int:course_id>/tugas', views.TugasView.as_view(), name='tugas'),    
    path('mata-kuliah/<int:course_id>/tugas/<int:task_id>/detail', views.TugasDetailView.as_view(), name='tugas-detail')
]