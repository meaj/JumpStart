from django.db import models

# Create your models here.
class faculty(models.Model):
    title = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    faculty_email = models.EmailField


class attendee(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    attendee_email = models.EmailField


class workshop(models.Model):
    survery_title =models.CharField(max_length=45)
    survey_body_information = models.CharField(max_length=1000)
    attendees = models.ForeignKey(attendee, on_delete=models.CASCADE)

