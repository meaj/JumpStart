from django.conf.urls import url
from . import views

app_name = 'workshop'

urlpatterns = [
    url(r'^create/', views.createWorkshop, name='create_workshop'),
    url(r'^(?P<pk>[0-9]+)/csv_upload', views.csv_upload_page, name='csv_upload'),
    url(r'^(?P<pk>[0-9]+)/createSession', views.createSession, name='createSession'),
    url(r'^(?P<pk>[0-9]+)/bulkemail', views.bulk_email_page, name='bulkemail'),
    url(r'^(?P<pk>[0-9]+)/', views.workshop_details, name='workshopdetails'),
]