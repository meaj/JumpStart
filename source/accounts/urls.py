from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signUp, name='signup'),
    url(r'^login/', views.loginView, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
]