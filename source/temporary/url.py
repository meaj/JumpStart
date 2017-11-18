from django.conf.urls import include, url
from splash import views
from temporary import views as temporary_view

urlpatterns = [
    url(r'(?P<uuid>[0-9a-f\-]+)', temporary_view.temp_uuid_page),  # is basicallt localhost/temporary/regex
]
