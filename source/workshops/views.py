from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
import pdb

from django.shortcuts import render, get_object_or_404
from importing.models import attendee as AttendeeObject, csv_file as CSVObject
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from importing.forms import CSV_Form, Email_Template_Form
from workshops.forms import Session_Form
from temporary.models import \
    attendee_email_workshop_uuid_association as AssociationObject
import re
from django.contrib.auth.decorators import login_required
from . import models
from .models import Workshop, session as SessionObject

from django.utils import datetime_safe
# Create your views here.


globalListOfAttenddes = []



@login_required(login_url='/login/')
def createWorkshop(request):
    if request.method == 'POST':
        if request.POST['title']:
            workshop = Workshop()
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

def workshop_details(request,pk):
        workshop = get_object_or_404(Workshop, pk=pk)
        workshop_associations = AssociationObject.objects.filter(workshop_local=workshop)
        sessions  = SessionObject.objects.filter(workshop=workshop)
        survey_list = models.Survey.objects.filter(workshop = workshop)
        survey = None
        for x in survey_list:
            survey = x

        attending = globalListOfAttenddes


        return render(request,'workshops/workshopdetails.html',{'workshop':workshop,
                                                                'workshop_associations':workshop_associations,
                                                                'sessions':sessions,
                                                                'survey': survey,
                                                                'attending':attending,
                                                                })


def createSession(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if(request.method =="POST"):
        form = Session_Form(request.POST)
        if form.is_valid():
            try :#object exists
               session = SessionObject.objects.get(workshop=workshop,session_title=form.cleaned_data['session_title'])
               error = 'session already exists'
               form = Session_Form()
               return render(request, 'workshops/createSession.html', {'error':error,'form':form})
            except:#object does not exist
                session = SessionObject.objects.create(workshop=workshop)
                session.session_title = form.cleaned_data['session_title']
                session.session_date = form.cleaned_data['session_date']
                session.session_location = form.cleaned_data['session_location']
                session.session_threshold = form.cleaned_data['session_threshold']
                session.save()
                return redirect('workshops/workshopdetails.html')
    #set values for session from form
    else:
        form = Session_Form()
        return render(request, 'workshops/createSession.html', {'workshop': workshop, 'form': form})



@login_required(login_url='accounts/login/')
def bulk_email_page(request, pk):
    if request.method == "POST":
        form = Email_Template_Form(request.POST)
        if form.is_valid():
            workshop = get_object_or_404(Workshop, pk=pk)
            workshop_associations = AssociationObject.objects.filter(workshop_local=workshop)
            survey = models.Survey.objects.all()
            last_survey = survey.reverse()[0]

            print(last_survey.id)
            for association in workshop_associations:
                temp_attendee = association.attendee_local
                #may need to change
                email_string = "http://" + str(
                    request.get_host()) + "/workshops/survey/" +str(last_survey.id)+ "/" +\
                    str(association.uuid_token)


#survey/(?P<survey_id>\d+)/(?P<uuid>[0-9a-f\-]+)


                temp_body = form.cleaned_data['email_body'] + "\nPlease take your survey here!:\n" + email_string + "\n\n" + form.cleaned_data['email_signature'] + "\n"



                send_mail(
                    form.cleaned_data['email_subject'],
                    temp_body,
                    form.cleaned_data['email_signature'],
                    [temp_attendee.email],
                    fail_silently=False
                )
                return redirect('/workshops/1/')


            # form.save()
            # email to a user
            # ensure that all fields are filled out or error
            # redirect page confirming success
    else:
        form = Email_Template_Form()
    return render(request, "email_template_page.html", {'form': form})


def process_file(form, f, workshop):
    # gets group name from form, will need to get from workshop in future, possibly rename to workshop name
    group_name = form.cleaned_data['group']
    #group_name = workshop.title should not be used as an invitee can be associated with multiple workshops

    for line in f:
        # Convert file bytes into string so that it can use split.
        lineS = str(line, 'utf-8')
        lineL = lineS.split(',')
        # attempts to split csv line into array with 12 indexes until EOF
        if len(lineL) != 12:
            # checks for abc123 in group instead, and possibly
            # overwrite existing db entry in case of email address change
            try:
                attendee = AttendeeObject.objects.get(utsa_id=lineL[6])
            except ObjectDoesNotExist:
                # checks to see if the first data member is a digit,
                # then checks that email and abc123 are vaild
                if re.match(r"\d+", lineL[0]) and re.match(
                        r"^[\w.]+@[\w.]+$", lineL[10]) \
                        and re.match(r"^[a-z]{3}[0-9]{3}$",
                                     lineL[6]):
                    attendee = AttendeeObject.objects.create(
                        utsa_id=lineL[6], last_name=lineL[7],
                        first_name=lineL[8],
                        email=lineL[10], group=group_name)
                    attendee.save()
                    try:
                        workshop_association = AssociationObject.objects.get(attendee_utsa_id=attendee.utsa_id,
                                                                             workshop_local=workshop)
                    except ObjectDoesNotExist:
                        workshop_association = AssociationObject.objects.create(attendee_local=attendee,
                                                                                attendee_utsa_id = attendee.utsa_id,
                                                                                workshop_local=workshop)
                        workshop_association.save()
                    else:
                        if(workshop_association.attendee != attendee):
                            workshop_association.attendee_local = attendee
                            workshop_association.attendee_clicked_link_local = False
                            workshop_association.save()
                else:
                    pass
            else:
                # If exception was not called and emails differ,
                # overwrite database entry's email and group name
                if re.match(r"\d+", lineL[0]) and re.match(
                        r"^[\w.]+@[\w.]+$",
                        lineL[10]) and attendee.email != lineL[10] \
                        and attendee.group != group_name:
                    attendee.email = lineL[10]
                    attendee.group = group_name
                    attendee.save()
                    # create association between workshop and attendee after import attempt
                    # this should work once workshop object is implemented
                #import ipdb
                #ipdb.set_trace()
                try:
                    workshop_association = AssociationObject.objects.get(attendee_utsa_id=attendee.utsa_id, workshop_local= workshop)
                except ObjectDoesNotExist:
                    workshop_association = AssociationObject.objects.create(attendee_local=attendee,
                                                                            attendee_utsa_id = attendee.utsa_id,
                                                                            workshop_local=workshop)
                    workshop_association.save()
                else:
                    if(workshop_association.attendee_local != attendee):
                        workshop_association.attendee_local = attendee
                        workshop_association.attendee_clicked_link_local = False
                        workshop_association.save()



@login_required(login_url='accounts/login/')
def csv_upload_page(request,pk):
    success = ""
    if request.method == "POST":
        form = CSV_Form(request.POST, request.FILES)
        if form.is_valid():
            workshop = get_object_or_404(models.Workshop, pk=pk)
            process_file(form, request.FILES['document'], workshop)
            success = "Added Invitees to Workshop!"
            # redirect to page confirming success
            return redirect('workshops/workshopdetails.html')
    else:
        form = CSV_Form()
    workshop = get_object_or_404(Workshop, pk=pk)
    return render(request, "workshops/csv_upload.html", {'form': form,'workshop':workshop,'success':success})


pkval = -1
def createQuestionsForSurvey(request, pk=-1):
    global pkval

    print("Start of createQuestions "+str(pk)+"                    PKPKPKPKPKPK")

    if(int(pk) > -1):
        pkval = pk

    import ipdb

    if request.method == 'POST':
        print("IS A POST STATEMENT------------------")
        if request.POST['questions']:
            name_of_survey = request.POST.get('survey_title_form')
            #threshold = request.POST.get('threshold')

            workshop = models.Workshop.objects.all()
            first_workshop = workshop[0]


            survey = models.Survey.objects.create(title=name_of_survey,
                                                  creator="user",
                                                  pub_date=datetime_safe.datetime.today(),
                                                  threshold=0,
                                                  workshop=first_workshop
                                                  )



            question_dict = request.POST.getlist('questions')
            for row_question in question_dict:
                models.Question.objects.create(body_text=row_question, survey=survey)

        print("\nNewly created survey id == "+ str(survey.id) )
        if(int(pkval) > -1):
            return redirect('/workshops/'+str(pkval)+'/')
        else:
            return redirect('/')
    if request.method == 'GET':
        print("I hate my life")


        return render(request, 'workshops/survey.html')
      # return redirect('/workshops/workshops/survey.html', {'pk': pk})


    else:
        print("Not a post statement "+"                    SDADSA")
        return render(request, 'workshops/survey.html')


def survey_render_function(request, survey_id, uuid):
    print(uuid)
    if request.method == "POST":

      #  ipdb.set_trace()
        answered_questions = {(key, value) for key, value in request.POST.dict().items() if 'question' in key}
        total = 0
        num_questions = len(answered_questions)

        survey = models.Survey.objects.filter(id=survey_id)
        threshold = 0.0

        local_sessions = SessionObject.objects.all()


        for value in survey:
            threshold = value.threshold
       # ipdb.set_trace()
        for key, value in answered_questions:
            total += int(value)

        averaged_score = float(total / num_questions)
        sessionList = []
        print("sessionList")
        for session in local_sessions:
            print("session threshold " +str(session.session_threshold))
            if session.session_threshold >= averaged_score:
                #show this session as available to student
                sessionList.append(session)
                list_of_association = AssociationObject.objects.filter(uuid_token_local = uuid)
                assoc_obj = list_of_association[0]
                #print(assoc_obj.attendee_local.email)
                global globalListOfAttenddes
                print(assoc_obj.attendee_local.email)
                if( assoc_obj.attendee_local.email not in globalListOfAttenddes):
                    globalListOfAttenddes.append(assoc_obj.attendee_local.email)
                    print(assoc_obj.attendee_local.email)
                #globalListOfAttenddes



        return render(request, 'workshops/complete_survey.html', {"total": total,
                                                                  "avg": float(total / num_questions),
                                                                  "num_questions": num_questions,
                                                                "threshold": threshold,
                                                                  "sessionList":sessionList
                                                                })


    else:
        questions = models.Question.objects.filter(survey__id=survey_id)
        form_values = models.AnsweredQuestions.KNOWLEDGE_IN_SUBJECT

        return render(request, 'workshops/present_survey.html', {'form': form_values,
                                                                 'survey_id': survey_id,
                                                                 'list_of_questions': questions,
                                                                 'uuid':uuid
                                                                 })
