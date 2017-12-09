from django.conf.urls import url
from . import views

app_name = 'workshop'

urlpatterns = [
    url(r'^create/', views.createWorkshop, name='workshops'),
    url(r'^(?P<pk>[0-9]+)/workshopdetails', views.workshop_details, name='workshopdetails'),
]