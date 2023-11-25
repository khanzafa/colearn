from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'lecturer'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.instructor}'

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    time = models.TimeField()
    venue = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.course} - {self.day} - {self.time}'

class Presence(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    meet_number = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(default=None, null=True, blank=True)
    end_time = models.TimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.course} - {self.date}'

class PresenceHistory(models.Model):
    presence = models.ForeignKey(Presence, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'student'})    
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.presence} - {self.student}'