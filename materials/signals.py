# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Material, MaterialHistory
from enrollments.models import Enrollment
from users.models import Student

@receiver(post_save, sender=Material)
def create_material_history(sender, instance, created, **kwargs):
    # Get all students enrolled in the course
    enrolled_students = Enrollment.objects.filter(course=instance.course).values_list('user', flat=True)
    enrolled_students = Student.objects.filter(user__in=enrolled_students)

    # Update or create MaterialHistory entries for each student
    for student in enrolled_students:
        MaterialHistory.objects.update_or_create(material=instance, student=student, defaults={'is_read': False})
