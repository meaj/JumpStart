from django.shortcuts import render
from temporary.models import attendee_email_workshop_uuid_association


# Create your views here.
def temp_uuid_page(request, uuid):
    '''
    Retreive data from here
    uuid is being shipped to here
    '''
    # needs to confirm it has arrived

    print(uuid)
    list_of_aewua = attendee_email_workshop_uuid_association.objects.all()
    for attendee_workshop in list_of_aewua:
        print(str(attendee_workshop.uuid_token) + " vs " + str(uuid))
        if str(uuid) == str(attendee_workshop.uuid_token):
            attendee_workshop.attendee_clicked_link()
            attendee_workshop.save()
            # attendee_full_name = attendee_workshop.attendee.first_name + " " + attendee_workshop.attendee.last_name
            #  workshop_name =  attendee_workshop.workshop.survery_title
            # No attendee objects and no workshop objects currently created to test data
            return render(request, "thanks_for_registering.html", {'uuid_name': str(attendee_workshop.uuid_token)})
    return render(request, "unknown_uuid.html", {})
