from django.contrib import admin
from courses.models import Course, Schedule, Presence, PresenceHistory

# Register your models here.
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Presence)
admin.site.register(PresenceHistory)
