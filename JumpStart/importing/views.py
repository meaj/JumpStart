from django.shortcuts import render
from importing.models import attendee as AttendeeObject, csv_file as CSVObject
from django.core.exceptions import ObjectDoesNotExist
from importing.forms import CSV_Form
import re

# Create your views here.
def csv_upload_page(request):
    if request.method == "POST":
        form = CSV_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            with open('media/csv_files/' + request.FILES['document'].name) as f:
                # gets group name from form
                group_name = form.cleaned_data['group']


                for line in f:
                    #attempts to split csv line into array wiht 12 indexes until EOF
                    data = line.split(",")
                    if len(data) != 12:
                        #checks to see if there is a group member with current email already, if so removes
                        #TODO: needs to change to check for abc123 in group instead, and possibly overrite existing db entry in case of email address change
                        try:
                            a = AttendeeObject.objects.get(group=group_name, email=data[10])
                        except ObjectDoesNotExist:
                            #checks to see if the first data member is a digit, then checks that email and abc123 are vaild
                            if re.match(r"\d+",data[0]) and re.match(r"^[\w\.]+@[\w\.]+$", data[10]) \
                                        and re.match(r"^[a-z]{3}[0-9]{3}$", data[6]):
                                AttendeeObject.objects.create(utsa_id=data[6], last_name=data[7], first_name=data[8],
                                                              email=data[10], group=group_name)
                            else:
                                pass
            #close csv file and remove csv models and files
            f.close()
            #alternative method if needed:
            #csv_file_objects = CSVObject.objects.all()
            #for c in csv_file_objects:
            c = CSVObject.objects.get()
            try:
                c.document.delete()
            except:
                pass
            c.delete()

    else:
        form = CSV_Form()
    return render(request, "csv_upload.html", {'form':form})
