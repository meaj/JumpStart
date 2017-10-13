from django.conf.urls import include, url
from importing import views

urlpatterns = [
    url(r'csv_upload', views.csv_upload_page, name='csv_upload'),
    ]