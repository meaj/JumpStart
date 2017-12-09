"""JumpStart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from splash.views import \
    index  # probably bad coding practice but, it defaults to a "splash" screen

admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
import accounts.views
import workshops.views
import importing.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^splash/', include('splash.url')),
    url(r'^temporary/', include('temporary.url')),
    url(r'^csv_upload', importing.views.csv_upload_page, name='csv_upload'),
    url(r'^email_template', importing.views.email_template_page,
        name='email_template'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', index, name='index'),  # goes to splash.views.index and loads splash_index_page, bad coding practive
    url(r'^workshops/', include('workshops.urls')),
    url(r'^$', index, name='index'),
    # goes to splash.views.index and loads splash_index_page, bad coding practive
    url(r'^workshops/', workshops.views.createWorkshop, name='workshops'),
]