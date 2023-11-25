from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='tasks/attachments/', default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class TaskSubmission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='tasks/submissions/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(default=0)
    comment = models.TextField(default='')

    def __str__(self):
        return self.task.title + ' - ' + self.student.username

