from django.contrib import admin

# Register your models here.

from .models import faculty, attendee, workshop

admin.site.register(faculty)
admin.site.register(attendee)
admin.site.register(workshop)