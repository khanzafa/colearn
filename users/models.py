from django.db import models
from django.contrib.auth.models import AbstractUser
# import pillow

# class CustomUser(AbstractUser):
#     email = models.EmailField(max_length=255, unique=True)  # Menggunakan EmailField untuk alamat email
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)  # Menggunakan ForeignKey untuk peran (lihat catatan di bawah)
#     photo = models.ImageField(upload_to='images/', default='images/default.png')

#     def __str__(self):
#         return self.username

# # Menambahkan model Role untuk mengelola peran pengguna
# class Role(models.Model):
#     name = models.CharField(max_length=100, unique=True)  # Menambahkan unik constraint pada nama peran
#     # Tambahkan izin-izin lainnya yang diperlukan untuk peran

# # Menghubungkan CustomUser dengan Role menggunakan ForeignKey
# CustomUser.role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)