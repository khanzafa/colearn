from django.db import models
from courses.models import Course
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Quiz(models.Model):
    quiz_type = (
        ('exercise', 'Exercise'),
        ('test', 'Test'),
    )
    quiz_type = models.CharField(max_length=20, choices=quiz_type, default='exercise')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=Course.objects.first().id)
    title = models.CharField(max_length=200)
    description = models.TextField()    
    duration = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'student'})
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} - {self.question} - {self.choice}'

class QuizHistory(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'student'})
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.student} - {self.quiz} - {self.score}'