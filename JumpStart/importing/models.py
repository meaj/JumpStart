from django.db import models
from django.test import TestCase


# Create your models here.




class faculty(models.Model):
    title = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    faculty_email = models.EmailField

    def __str__(self):
        return  self.title + " " + self.last_name

class attendee(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=60)
    attendee_email = models.EmailField
    def __str__(self):
        return self.email

class workshop(models.Model):
    survey_title = models.CharField(max_length=45)
    survey_body_information = models.CharField(max_length=1000)
    attendees = models.ForeignKey(attendee, on_delete=models.CASCADE)
    def __str__(self):
        return self.survey_title

class email_template(models.Model):
    email_name = models.CharField(max_length=16,default="name")
    email_subject = models.CharField(max_length=48, default="subject")
    email_body = models.TextField(max_length=2000, default="body")
    email_signature = models.CharField(max_length=48, default="jumpstartutsa@gmail.com")
    def __str__(self):
        return self.email_name
