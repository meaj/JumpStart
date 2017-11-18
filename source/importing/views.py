from django.shortcuts import render
from importing.models import attendee as AttendeeObject, csv_file as CSVObject
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from importing.forms import CSV_Form, Email_Template_Form
from temporary.models import attendee_email_workshop_uuid_association as AssociationObject
import re
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def email_template_page(request):
    if request.method == "POST":
        form = Email_Template_Form(request.POST)
        if form.is_valid():
            form.save()
            # ensure that all fields are filled out or error
            # redirect page confirming success
    else:
        form = Email_Template_Form()
    return render(request, "email_template_page.html", {'form': form})


@login_required(login_url='/login/')
def csv_upload_page(request):
    if request.method == "POST":
        form = CSV_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # need to get workshop to be associated with these attendees
            # possibly take as an argument?
            with open('media/csv_files/' + request.FILES['document'].name) as f:
                # gets group name from form, will need to get from workshop in future, possibly rename to workshop name
                group_name = form.cleaned_data['group']

                for line in f:
                    # attempts to split csv line into array wiht 12 indexes until EOF
                    data = line.split(",")
                    if len(data) != 12:
                        # checks for abc123 in group instead, and possibly
                        # overrite existing db entry in case of email address change
                        try:
                            attendee = AttendeeObject.objects.get(utsa_id=data[6])
                        except ObjectDoesNotExist:
                            # checks to see if the first data member is a digit,
                            # then checks that email and abc123 are vaild
                            if re.match(r"\d+", data[0]) and re.match(r"^[\w.]+@[\w.]+$", data[10]) \
                                    and re.match(r"^[a-z]{3}[0-9]{3}$", data[6]):
                                attendee = AttendeeObject.objects.create(utsa_id=data[6], last_name=data[7],
                                                                         first_name=data[8],
                                                                         email=data[10], group=group_name)
                            else:
                                pass
                        # If multiple abc123 attendees are detected, unexpected behavior based on database conflicts,
                        # delete all found and create new from file
                        except MultipleObjectsReturned:
                            attendees = AttendeeObject.objects.all()
                            for a in attendees:
                                a.delete()
                            if re.match(r"\d+", data[0]) and re.match(r"^[\w.]+@[\w.]+$", data[10]) \
                                    and re.match(r"^[a-z]{3}[0-9]{3}$", data[6]):
                                attendee = AttendeeObject.objects.create(utsa_id=data[6], last_name=data[7],
                                                                         first_name=data[8],
                                                                         email=data[10], group=group_name)
                            else:
                                pass
                        else:
                            # If exception was not called and emails differ,
                            # overwrite database entry's email and group name
                            if re.match(r"\d+", data[0]) and re.match(r"^[\w.]+@[\w.]+$",
                                                                      data[10]) and attendee.email != data[10] \
                                    and attendee.group != group_name:
                                attendee.email = data[10]
                                attendee.group = group_name
                                attendee.save()

                                # create association between workshop and attendee after import attempt
                                # this should work once workshop object is implemented
                                # association = AssociationObject.objects.create()
                                # association.setup_association(attendee, workshop)

            # close csv file and remove csv models and files
            f.close()

            csv_file_objects = CSVObject.objects.all()
            for c in csv_file_objects:
                c.document.delete()
            # redirect to page confirming success

    else:
        form = CSV_Form()
    return render(request, "csv_upload.html", {'form': form})
