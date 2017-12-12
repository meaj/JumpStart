from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Workshop(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    owner = models.ForeignKey(User, default="Admin")

    def __str__(self):
        return self.title

class session(models.Model):
    session_title = models.CharField(max_length=48,default="title")
    session_date = models.DateTimeField(default="1987-01-01 00:00")
    session_location = models.CharField(max_length=48,default="CS Main Lab")
    session_threshold = models.IntegerField(default= 1)
    workshop = models.ForeignKey(Workshop, default=1)