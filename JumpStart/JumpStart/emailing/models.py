from django.db import models
from django.core.mail import send_mail
# Create your models here.

#feel free to refactor if you have better names

class email_object:
    def __init__(self):
        self._subject = ""
        self._message = ""
        self._email_sender = "jumpstartutsa@gmail.com" #can change later
        self._target_email_addresses = []

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, input_subject):
       self._subject = input_subject

    @property
    def email_sender(self):
        return self._message

    @email_sender.setter
    def email_sender(self, input_email_sender):
       self._email_sender = input_email_sender

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, input_message):
       self._message = input_message

    @property
    def target_email_addresses(self):
        return self._message

    @target_email_addresses.setter
    def target_email_addresses(self, input_target_email_addresses):
       self._target_email_addresses = input_target_email_addresses

    def add_email_to_target_email_addresses(self, email ):
        self._target_email_addresses.append(email)

    def remove_email_to_taget_email_addresses(self, email ):
       self._target_email_addresses.remove(email)

    def send_email(self):
        send_mail(
            self._subject, #Email Subject field
            self._message, #Email Message
            self._email_sender, #Sender of Email
            self._target_email_addresses, #Target Email Address
                fail_silently=False)