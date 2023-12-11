from django.db import models
from common.utils import generate_pdf_thumbnail
from courses.models import Course
from users.models import Student
from .apps import MaterialsConfig
import os
from django.conf import settings
app_name = MaterialsConfig.name

# Create your models here.
class Material(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()    
    file = models.FileField(upload_to='materials/uploads/')
    thumbnail = models.ImageField(upload_to='materials/thumbnails/', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.file.name.lower().endswith('.pdf') and not self.thumbnail:
            file_name = os.path.splitext(os.path.basename(self.file.name))[0]
            pdf_path = self.file.path
            thumbnail_dir = os.path.join(settings.MEDIA_ROOT, 'materials/thumbnails')
            os.makedirs(thumbnail_dir, exist_ok=True)            
            generate_pdf_thumbnail(pdf_path, thumbnail_dir)
            self.thumbnail = os.path.join('materials/thumbnails', f'{file_name}_thumbnail.png')
            super().save(update_fields=['thumbnail'])

    def __str__(self):
        return self.title

class MaterialHistory(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.material} - {self.student}'