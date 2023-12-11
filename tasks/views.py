from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task, TaskSubmission
from django.views import View
from courses.models import Course
from django.db import models

# Create your views here.
class TugasView(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        tasks = Task.objects.filter(course_id=course_id)
        tasks = tasks.annotate(
            is_submitted=models.Exists(
                TaskSubmission.objects.filter(task_id=models.OuterRef('pk'), student_id=request.user.id)
            )
        )
        return render(request, 'tugas.html', {
            'course': course,
            'tasks': tasks
        })
        # return JsonResponse({
        #     'course': course.title,
        #     'tasks': [task.title for task in tasks]
        # })

class TugasDetailView(View):
    def get(self, request, course_id, task_id):
        course = Course.objects.get(pk=course_id)
        task = Task.objects.get(pk=task_id)
        task_submission = TaskSubmission.objects.filter(task_id=task.id, student_id=request.user.id).first()        
        return render(request, 'detail-tugas.html', {
            'course': course,
            'task': task,
            'task_submission': task_submission
        })

        # return JsonResponse({
        #     'course': task.course.title,
        #     'task': task.title,
        #     'task_submission': task_submission.attachment.url
        # })

    def post(self, request, course_id, task_id):
        task_submission = TaskSubmission.objects.create(
            task_id=task_id, 
            student_id=request.user.id,
            attachment=request.FILES.get('taskFile'),
            description=request.POST.get('taskDescription')
        )

        return redirect('tasks:tugas-detail', course_id=course_id, task_id=task_id)
        # return JsonResponse({
        #     'attachment': request.FILES.get('taskFile').name,  # Use .name to get the file name
        #     'description': request.POST.get('taskDescription')
        # })
