from django.shortcuts import render
from .models import Task, TaskSubmission

# Create your views here.
def tugas(request):
    tasks = Task.objects.all()
    return render(request, 'tugas.html', {
        'tasks': tasks
    })

def detailTugas(request):
    # task_id = request.GET.get('task_id')
    task_id = 1
    task = Task.objects.get(pk=task_id)
    # task_submission = TaskSubmission.objects.get(task_id=task.id)
    return render(request, 'detail-tugas.html', {
        'task': task
        # 'task_submission': task_submission
    })