from django.db import models
from django.contrib.auth.models import User
from importing import models as ImportingModels



# Create your models here.


class Workshop(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    owner = models.ForeignKey(User, default="Admin")

    def __str__(self):
        return self.title





class session(models.Model):
    session_title = models.CharField(max_length=48,default="title")
    session_location = models.CharField(max_length=48,default="CS Main Lab")
    session_date = models.DateTimeField(default="1987-01-01 00:00")
    session_threshold = models.IntegerField(default= 1)
    workshop = models.ForeignKey(Workshop, default=1)
    registered_attendees = models.ManyToManyField(ImportingModels.attendee, default=None)



    #This should create a many to many relationship between this session and the attendee to be registered
    def register(self,this_session, attendee_to_register):
        if type(attendee_to_register) == ImportingModels.attendee and type(this_session) == session:
            this_session.registered_attendees.add(attendee_to_register)
        return  self



class Survey(models.Model):
    title = models.CharField(max_length=60)
    creator = models.CharField(max_length=60)
    threshold = models.FloatField(max_length=3)
    pub_date = models.DateField()
    workshop = models.ForeignKey(Workshop)


    def __str__(self):
        return self.title


class Question(models.Model):
    body_text = models.TextField()
    survey = models.ForeignKey(Survey)

    def __str__(self):
        return self.body_text

from enum import Enum
class QuestionValues(Enum):
    NOKNOWLEDGE = 1
    VERYLITTLEKNOWLEDGE = 2
    SOMEKNOWLEDGE = 3
    Familiar = 4
    EXPERIENCED = 5


class AnsweredQuestions(models.Model):
    KNOWLEDGE_IN_SUBJECT = (
        (QuestionValues.NOKNOWLEDGE.value, 'No Knowledge'),
        (QuestionValues.VERYLITTLEKNOWLEDGE.value, 'Very little Knowledge'),
        (QuestionValues.SOMEKNOWLEDGE.value, 'Some'),
        (QuestionValues.Familiar.value, 'Familiar'),
        (QuestionValues.EXPERIENCED.value, 'Experienced'),
    )

    knowledge_scale = models.CharField(
        max_length=2,
        choices=KNOWLEDGE_IN_SUBJECT,
        default=QuestionValues.SOMEKNOWLEDGE.value,
    )

    question = models.ForeignKey(Question)

    def is_knowledge(self):
        return self.knowledge_scale in (self.NOKNOWLEDGE,
                                        self.VERYLITTLEKNOWLEDGE,
                                        self.SOMEKNOWLEDGE,
                                        self.Familiar,
                                        self.EXPERIENCED,
                                        )



