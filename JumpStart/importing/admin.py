from django.contrib import admin

# Register your models here.

from .models import faculty, attendee, workshop, email_template

admin.site.register(faculty)
admin.site.register(attendee)
admin.site.register(workshop)
admin.site.register(email_template)