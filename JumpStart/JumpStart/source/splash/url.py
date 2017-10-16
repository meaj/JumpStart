from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth.views import logout
from splash import views

urlpatterns = [
    url(r'thanks', views.thanks_for_sending_emails, name='thanks_for_sending_emails'),
    url(r'login', views.login_page, name='login_page'),
    url(r'login_present', views.login_present, name='login_present'),
    url(r'succesful_login', views.succesful_login, name='succesful_login'),
    url(r'authenticate_login', views.succesful_login, name='authenticate_login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^logged_out', views.logged_out, name= 'logged_out'),
    ]