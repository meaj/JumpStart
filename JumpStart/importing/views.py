from django.shortcuts import render
from importing.models import attendee as AttendeeObject
from django.core.files.storage import FileSystemStorage


# Create your views here.
def csv_import_page(request):
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #instead of just uploading a file, I want to generate new attendee database objects
        return render(request, "csv_upload.html", {'uploaded_file_url':uploaded_file_url})
    return render(request, 'csv_upload.html')