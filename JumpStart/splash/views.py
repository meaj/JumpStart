from django.shortcuts import render
from emailing.models import email_object
from temporary.models import attendee_email_workshop_uuid_association
from importing.models import attendee as atendeeObject, workshop as workshopObject
from .forms import NameForm
from .forms import EmailForm
from django.http import HttpResponseRedirect

# Create your views here.

#index
def thanks_for_sending_emails(request):
    return render(request, 'emails_have_been_sent.html', {})

def login_page(request):
    return render(request, 'login_page.html', {})

def index(request):

    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            '''
            the entry of the form is valid. The code called this function again so, but, its valid this time so we form
            data has been filled out and we can now acces it, we cannot access it if it is not valid

            '''
            temp_attendee = ""
            temp_workshop = ""
            temp_association = attendee_email_workshop_uuid_association()

            for attend in atendeeObject.objects.all():
                if attend.first_name == "kk" :
                    temp_attendee = attend

            for workshop in workshopObject.objects.all():
                if workshop.survery_title == "DAT WORKSHOP":
                    temp_workshop = workshop
            '''
            The for loops look weird because, we have to have models already committed to the database to run these
            this should be much less of an issue once we import csv's to create attendees and add in faculty, for now
            I've added these into the admin section. http://127.0.0.1:8000/admin/ is the current path and
            name is admin
            password is admin1234
            '''
            temp_association.setup_association(temp_attendee, temp_workshop)
            temp_association.save()

            for x in attendee_email_workshop_uuid_association.objects.all():
                print(str(x.uuid_token))

            local_subject = "this is test"

            email_string = "http://127.0.0.1:8000/temporary/" + str(temp_association.uuid_token)

            local_message = "this is the body text of the email\n hola mi amigo!\n " + email_string + "\n"
            local_email_sender = "jumpstartutsa@gmail.com"
            local_target_email_addresses = form.cleaned_data['attendee_email'] #This is the data pulled from the postform
            print(local_target_email_addresses)
            email = email_object()
            email.subject = local_subject
            email.message = local_message
            email.email_sender = local_email_sender
            #  email.target_email_addresses = local_target_email_addresses
            email.add_email_to_target_email_addresses(local_target_email_addresses)

            email.send_email()

            return HttpResponseRedirect('/splash/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, 'send_email_registrations.html', {'form': form})