from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models


# Create your views here.
@login_required(login_url='/login/')
def createWorkshop(request):
    if request.method == 'POST':
        if request.POST['title']:
            workshop = models.Workshop()
            workshop.title = request.POST['title']
            workshop.pub_date = timezone.datetime.now()
            workshop.owner = request.user
            workshop.save()
            return redirect('/?next=/')
        else:
            return render(request, 'workshops/workshops.html',
                          {'error': 'ERROR: You must include a Title'})
    else:
        return render(request, 'workshops/workshops.html')
