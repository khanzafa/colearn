from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Enrollment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, limit_choices_to={'role' : 'student'})
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'{self.user.username} enrolled in {self.course.title}'