from django.db import models
from courses.models import Course

# Create your models here.
class Material(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='materials/uploads/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Tambahkan bidang-bidang lain yang sesuai dengan kebutuhan Anda.
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

