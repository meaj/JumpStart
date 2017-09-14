from django.conf.urls import include, url
from splash import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    ]