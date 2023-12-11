from django.contrib.auth.models import AbstractUser
from django.db import models
from .apps import UsersConfig

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('lecturer', 'Lecturer'),
        ('student', 'Student'),
        ('admin', 'Administrator')
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username

app_name = UsersConfig.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE, primary_key=True)
    nim = models.CharField(max_length=20)
    GENDER_CHOICES = [
        ('laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
        ('tidak diketahui', 'Tidak diketahui')
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='tidak diketahui')
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=f'{app_name}/uploads/', default=f'{app_name}/uploads/default.png')

    def __str__(self):
        return self.user.username

class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, limit_choices_to={'role': 'lecturer'}, on_delete=models.CASCADE, primary_key=True)
    nip = models.CharField(max_length=20)
    faculty = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=f'{app_name}/uploads/', default=f'{app_name}/uploads/default.png')

    def __str__(self):
        return self.user.username