from django.shortcuts import render, redirect
from importing.models import attendee as AttendeeObject
from django.core.files.storage import FileSystemStorage
from importing.forms import CSV_Form

# Create your views here.
def csv_import_page(request):
    if request.method == "POST":
        form = CSV_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('index')
            #import csv into invitee object such that invitee -> emailing -> attendee
    else:
        form = CSV_Form()
    return render(request, "csv_upload.html", {'form':form})