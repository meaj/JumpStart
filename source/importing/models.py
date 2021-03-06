from django.db import models
import os
from django.test import TestCase


# Create your models here.

class faculty(models.Model):
    title = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    department = models.CharField(max_length=48)
    faculty_email = models.EmailField

    def __str__(self):
        return self.title + " " + self.last_name


class attendee(models.Model):
    group = models.CharField(max_length=48, default="group")
    utsa_id = models.CharField(max_length=6, default="abc123", primary_key=True)
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.CharField(max_length=60)
    attendee_email = models.EmailField

    def __str__(self):
        return self.group + " : " + self.email


'''#temporary session model
class session(models.Model):
    session_title = models.CharField(max_length=48,default="title")
    session_date = models.CharField(max_length=48,default="5 November")
    session_threshold = models.IntegerField(default= 1)

class workshop(models.Model):
    survey_title = models.CharField(max_length=48,default="title")
    survey_body_information = models.CharField(max_length=1000)
    attendees = models.ForeignKey(attendee, on_delete=models.CASCADE)
    def __str__(self):
        return self.survey_title
'''


class email_template(models.Model):
    email_name = models.CharField(max_length=16, default="name")
    email_subject = models.CharField(max_length=48, default="subject")
    email_body = models.TextField(max_length=2000, default="body")
    email_signature = models.CharField(max_length=48,
                                       default="jumpstartutsa@gmail.com")

    def __str__(self):
        return self.email_name


class csv_file(models.Model):
    description = models.CharField(max_length=46, blank=True)
    document = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
