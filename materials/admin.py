from django.contrib import admin
from .models import Material, MaterialHistory

# Register your models here.
admin.site.register(Material)
admin.site.register(MaterialHistory)