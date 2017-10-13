from django.shortcuts import render, redirect
from importing.models import attendee as AttendeeObject
from django.core.exceptions import ObjectDoesNotExist
from importing.forms import CSV_Form, Import_Form
import csv

# Create your views here.
def csv_upload_page(request):
    if request.method == "POST":
        form = CSV_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            with open('media/csv_files/' + request.FILES['document'].name) as f:
                group_name = request.FILES['document'].name  # get group name from user in future instead of using this method

                # need to check lines to see if they have correct format
                # maybe "re.match(.*, {12}.*)" and keep first result as header?
                reader = csv.reader(f, delimiter=',')
                header = next(reader) #header currently not used
                for row in reader:
                    # checks to see if an attendee with given email exists in current group
                    try :
                        a = AttendeeObject.objects.get(group=group_name, email=row[10])
                    except ObjectDoesNotExist:
                        AttendeeObject.objects.create(utsa_id=row[6],
                                                      last_name=row[7],
                                                      first_name=row[8],
                                                      email=row[10],
                                                      group=group_name)
                    else:
                        pass
    else:
        form = CSV_Form()
    return render(request, "csv_upload.html", {'form':form})