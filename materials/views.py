from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Material, MaterialHistory
from courses.models import Course
from django.views import View

# Create your views here.
class MateriView(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)   
        materials = Material.objects.filter(course_id=course_id)
        material_historys = MaterialHistory.objects.filter(student_id=request.user.id, material_id__in=materials.values_list('id', flat=True))
        return render(request, 'materi.html', {
            'course': course,
            'materials': materials,
            'material_historys': material_historys
        })

        # return JsonResponse({
        #     'course': course.title,            
        #     'material_historys': [material_history.is_read for material_history in material_historys],
        #     'materials': [material_history.material.title for material_history in material_historys],
        # })

    def post(self, request, course_id, material_id):
        material = Material.objects.get(pk=material_id)
        material_history = MaterialHistory.objects.filter(material_id=material_id, student_id=request.user.id)
        if not material_history:
            MaterialHistory.objects.create(
            material_id=material_id,
            student_id=request.user.id,
            is_read=True
        )                
        else:
            material_history.update(is_read=True)
                        
        return redirect('materials:materi', course_id=course_id)

class MateriDetailView(View):
    def get(self, request, course_id, material_id):
        material = Material.objects.get(pk=material_id)
        return render(request, 'detail-materi.html', {
            'material': material
        })