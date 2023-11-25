from django.shortcuts import render
from django.http import HttpResponse
from .models import Course, Schedule, Presence, PresenceHistory
from tasks.models import Task
from materials.models import Material
from quizzes.models import Quiz
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def matkul(request):
    # return HttpResponse('Halo, kamu sedang berada di halaman mata kuliah.')
    courses = Course.objects.all()
    schedule = Schedule.objects.all()
    return render(request, 'matkul.html', {
        'courses': courses,
        'schedule': schedule
    })

def detailMatkul(request):
    # course_id = request.GET.get('course_id')
    course_id = 1
    course = Course.objects.get(pk=course_id)
    schedule = Schedule.objects.get(course_id=course.id)
    presence = Presence.objects.get(course_id=course.id)
    # presence_history = PresenceHistory.objects.get(presence_id=presence.id, student_id=request.user.id)
    instructor = User.objects.get(pk=course.instructor_id)
    material = Material.objects.get(course_id=course.id)
    task = Task.objects.get(course_id=course.id)
    quiz = Quiz.objects.get(course_id=course.id)
    # return HttpResponse('Halo, kamu sedang melihat mata kuliah %s.' % course)
    return render(request, 'detail-matkul.html', {
        'course': course,
        'schedule': schedule,
        'presence': presence,
        # 'presence_history': presence_history,
        'instructor': instructor,
        'material': material,
        'task': task,
        'quiz': quiz
    })

