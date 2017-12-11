from django.db import models
from importing.models import attendee as attendeeObject
from workshops.models import Workshop as workshopObject
import uuid


# Create your models here.

def generate_uuid():
    return uuid.uuid4()


class attendee_email_workshop_uuid_association(models.Model):
    attendee_utsa_id = models.CharField(max_length=6, default="abc123")
    uuid_token_local = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                        editable=False)
    attendee_local = models.ForeignKey(attendeeObject, on_delete=models.CASCADE,
                                       default=1)
    workshop_local = models.ForeignKey(workshopObject, on_delete=models.CASCADE,
                                       default=1)
    attendee_clicked_link_local = models.BooleanField(default=False)

    @property
    def uuid_token(self):
        return self.uuid_token_local

    @property
    def attendee(self):
        return self.attendee_local

    @property
    def utsa_id(self):
        return self.attendee_utsa_id

    @property
    def workshop(self):
        return self.workshop_local


    def setup_association(self, intput_attendee, input_workshop):
        if (
                intput_attendee is attendeeObject and input_workshop is workshopObject):
            self.attendee_local = intput_attendee
            self.workshop_local = input_workshop

    def check_if_same_uuid(self, incoming_uuid):
        if (incoming_uuid is uuid):
            if (str(incoming_uuid) == str(self.uuid_token)):
                return True
            else:
                return False
        else:
            return False

    def attendee_clicked_link(self):
        self.attendee_clicked_link_local = True
