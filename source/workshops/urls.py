from django.conf.urls import url
from . import views

app_name = 'workshop'

urlpatterns = [
    url(r'^create/', views.createWorkshop, name='create_workshop'),
    url(r'^(?P<pk>[0-9]+)/csv_upload', views.csv_upload_page, name='csv_upload'),
    url(r'^(?P<pk>[0-9]+)', views.workshopdetails, name='workshopdetails'),
    url(r'^email_template', views.email_template_page,
        name='email_template'),
]