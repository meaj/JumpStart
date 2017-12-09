from django.conf.urls import include, url
from splash import views

urlpatterns = [
    url(r'thanks', views.thanks_for_sending_emails,
        name='thanks_for_sending_emails'),
]
