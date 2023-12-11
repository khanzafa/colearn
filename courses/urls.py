from django.urls import path, include
from courses import views

app_name = 'courses'
urlpatterns = [
    path('mata-kuliah', views.MataKuliahView.as_view(), name='mata-kuliah'),
    path('mata-kuliah/<int:course_id>/detail/', views.MataKuliahDetailView.as_view(), name='mata-kuliah-detail'),
    path('mata-kuliah/presence/<int:presence_id>', views.MataKuliahDetailView.as_view(), name='mata-kuliah-presence')
]