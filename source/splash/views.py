from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from temporary.models import attendee_email_workshop_uuid_association
from importing.models import attendee as atendeeObject, email_template as emailObject

from .forms import EmailForm
from workshops import models as workshopObject


# index
@login_required(login_url='accounts/login/')
def thanks_for_sending_emails(request):
    return render(request, 'emails_have_been_sent.html', {})


@login_required(login_url='accounts/login/')
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
                if attend.first_name == "kk":
                    temp_attendee = attend

            for workshop in workshopObject.Workshop.objects.all():
                if workshop.title == "DAT WORKSHOP":
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
            email_string = "http://" + str(request.get_host()) + "/temporary/" + str(temp_association.uuid_token)
            local_message = "this is the body text of the email\n hola mi amigo!\n " + email_string + "\n"
            local_email_sender = "jumpstartutsa@gmail.com"
            local_target_email_addresses = form.cleaned_data[
                'attendee_email']  # This is the data pulled from the postform

            ''' 
                This allows the email to read the data stored in the email_templates database
                needs to be changed to use specific email template from list of available templates
            '''
            for e in emailObject.objects.all():
                if e.email_name == "template1":
                    local_subject = e.email_subject
                    local_message = e.email_body + "\nYour unique email link is:\n" + email_string + "\n\n" + e.email_signature + "\n"

            print(local_target_email_addresses)

            send_mail(
                local_subject,
                local_message,
                local_email_sender,
                [local_target_email_addresses],
                fail_silently=False
            )

            return HttpResponseRedirect('/splash/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()
    workshops = workshopObject.Workshop.objects.all()
    return render(request, 'send_email_registrations.html', {'form': form, 'workshops': workshops})
