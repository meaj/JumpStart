from django.conf.urls import include, url
from importing import views

urlpatterns = [
    url(r'^$', views.csv_upload_page, name='csv_upload'),
    ]