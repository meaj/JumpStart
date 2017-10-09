from django.shortcuts import render, redirect
from importing.models import attendee as AttendeeObject
from django.core.files.storage import FileSystemStorage
from importing.forms import CSV_Form, Import_Form
import csv

# Create your views here.
def csv_upload_page(request):
    if request.method == "POST":
        form = CSV_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('index')
    else:
        form = CSV_Form()
    return render(request, "csv_upload.html", {'form':form})

#prototype version of csv importing, needs to get file name from import_form
def csv_import_page(request):
    if request.method == "POST": #using post since we will be adding to the attendee database
        form = Import_Form(request.POST, request.FILES)
        with open('media/csv_files/file1.csv') as f:
            group_name = "default" #get group name from form
            #need to check lines to see if they have correct format
            #maybe "re.match(.*, {12}.*)" and keep first result as header?
            reader = csv.reader(f, delimiter=',')
            header = next(reader)
            for row in reader:
                #needs conditional to ensure utsa_id and email are populated at least
                #possibly change to bulk_create
                AttendeeObject.objects.create(utsa_id=row[6],
                                              last_name=row[7],
                                              first_name = row[8],
                                              email=row[10],
                                              group=group_name)
    #need to create csv_import.html
    else : form = Import_Form()
    return render(request, "csv_import.html", {'form':form})