from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('lecturer', 'Lecturer'),
        ('student', 'Student'),
        ('admin', 'Administrator')
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='student')
    # photo = models.ImageField(upload_to='images/', default='images/default.png')

    def __str__(self):
        return self.username
