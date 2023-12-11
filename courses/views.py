from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Course, Schedule, Presence, PresenceHistory
from users.models import Student, Lecturer
from tasks.models import Task
from materials.models import Material
from quizzes.models import Quiz
from enrollments.models import Enrollment
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
User = get_user_model()

# Create your views here.
class MataKuliahView(View):
    def get(self, request):
        enrollments = Enrollment.objects.filter(user_id=request.user.id)
        courses = Course.objects.filter(id__in=enrollments.values_list('course_id', flat=True))        
        # return JsonResponse({
        #     'courses': [course.title for course in courses],
        #     'instrukturs': [course.instructor.first_name + course.instructor.last_name for course in courses],
        # })

        return render(request, 'matkul.html', {
            'courses': courses,
        })


class MataKuliahDetailView(View):
    def get(self, request, course_id):
        # Menggunakan get_object_or_404 untuk menghindari kegagalan jika objek tidak ditemukan
        course = get_object_or_404(Course, pk=course_id)
        schedule = get_object_or_404(Schedule, course_id=course.id)
        instructor = get_object_or_404(User, pk=course.instructor_id)
        lecturer = get_object_or_404(Lecturer, user_id=course.instructor_id)

        presences = Presence.objects.filter(course_id=course.id)    
        presence_historys = PresenceHistory.objects.filter(presence_id__in=presences.values_list('id', flat=True), student_id=request.user.id)
        live_presence = Presence.objects.filter(course_id=course.id, date__gte=timezone.now().date(), end_time__gte=timezone.now().time()).first()
        
        # Memeriksa keberadaan live_presence_history
        if live_presence:
            live_presence_history = PresenceHistory.objects.get(presence_id=live_presence.id, student_id=request.user.id)
            if live_presence_history.is_present:
                live_presence = None

        materials = Material.objects.filter(course_id=course.id)
        material_count = materials.count()
        recent_material = materials.last().created_at
        task = Task.objects.filter(course_id=course.id)
        task_count = task.count()
        recent_task = task.last().created_at
        quiz = Quiz.objects.filter(course_id=course.id)
        quiz_count = quiz.count()
        recent_quiz = quiz.last().created_at

        enrollments = Enrollment.objects.filter(course_id=course.id)
        users = User.objects.filter(id__in=enrollments.values_list('user_id', flat=True))
        students = Student.objects.filter(user_id__in=users.values_list('id', flat=True))

        # return JsonResponse ({
        #     'live_presences' : live_presences.date,
        #     'time_now' : timezone.now(),
        # })

        return render(request, 'detail-matkul.html', {
            'course': course,
            'schedule': schedule,
            'presences': presences,
            'presence_historys': presence_historys.order_by('-presence__date'),
            'instructor': instructor,
            'materials': materials,
            'task': task,
            'quiz': quiz,
            'material_count': material_count,
            'task_count': task_count,
            'quiz_count': quiz_count,
            'recent_material': recent_material,
            'recent_task': recent_task,
            'recent_quiz': recent_quiz,
            'users': users,
            'students': students,
            'lecturer': lecturer,
            'live_presence': live_presence,
        })
    
    def post(self, request, presence_id):
        # Menggunakan get_object_or_404 untuk menghindari kegagalan jika objek tidak ditemukan
        presence = get_object_or_404(Presence, pk=presence_id)
        course = get_object_or_404(Course, pk=presence.course_id)

        # Memastikan bahwa presensi belum pernah diisi oleh student tertentu
        if not PresenceHistory.objects.filter(presence_id=presence.id, student_id=request.user.id).exists():
            presence_history = PresenceHistory.objects.create(presence_id=presence.id, student_id=request.user.id, is_present=True)
            presence_history.save()
        
        return redirect('courses:mata-kuliah-detail', course_id=course.id)


