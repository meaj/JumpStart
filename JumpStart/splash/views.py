from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#index
def index(request):
    return render(request, "splash_index_page.html", {})