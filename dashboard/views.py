from django.shortcuts import render
from django.http import JsonResponse
from .models import Announcement
from users.models import Student, Lecturer
from materials.models import Material
from quizzes.models import Quiz
from tasks.models import Task
from courses.models import PresenceHistory
from enrollments.models import Enrollment
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def dashboard(request):
    student = Student.objects.get(user=request.user.id)
    announcements = Announcement.objects.all()

    courses = Enrollment.objects.filter(user=student.user)
    courses = [course for course in courses]

    material_count = 0
    task_count = 0
    quiz_count = 0
    for course in courses:
        material_count += Material.objects.filter(course=course.course).count()
        task_count += Task.objects.filter(course=course.course).count()
        quiz_count += Quiz.objects.filter(course=course.course).count()

    presence_history_count = PresenceHistory.objects.filter(student=student, is_present=True).count()    
    total_presence_history_count = PresenceHistory.objects.filter(student=student).count()
    
    return render(request, 'dashboard.html', {
        'student': student,
        'announcements': announcements,
        'material_count': material_count,
        'task_count': task_count,
        'quiz_count': quiz_count,
        'presence_history_count': presence_history_count,
        'total_presence_history_count': total_presence_history_count
    })    


    # return JsonResponse({
    #     'student': student.user.username,
    #     'announcements': [announcement.title for announcement in announcements],
    #     'material_count': material_count,
    #     'task_count': task_count,
    #     'quiz_count': quiz_count,
    #     'presence_percentage': presence_percentage
    # })