from django.urls import path, include
from materials import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'materials'
urlpatterns = [ 
    path('mata-kuliah/<int:course_id>/materi', views.MateriView.as_view(), name='materi'),
    path('mata-kuliah/<int:course_id>/materi/<int:material_id>/mark-as-read', views.MateriView.as_view(), name='materi-terbaca'),
    path('mata-kuliah/<int:course_id>/materi/<int:material_id>/detail', views.MateriDetailView.as_view(), name='materi-detail')
]