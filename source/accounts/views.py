from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from accounts.forms import *


def signUp(request):

    #if the user sends infor its a post request
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
             return createUserIfDoesNotExist(request)
        else:
            return render(request, 'accounts/signUp.html', {'error': 'Passwords didn\'t match'})
    else:# its a get request
        return render(request, 'accounts/signUp.html')

def loginView(request):
    #if the user sends infor its a post request
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            #redirect to succes page
            return render(request, 'accounts/login.html', {'error': 'succesfull login'})
        else:
            #invalid user
            return render(request, 'accounts/login.html', {'error': 'the username and password didn\'t match'})
    else:# its a get request
        return render(request, 'accounts/login.html')



def createUserIfDoesNotExist(request):
    try:
        User.objects.get(username = request.POST['username'])
        return render(request, 'accounts/signUp.html', {'error': 'Username has already been taken'})
    except User.DoesNotExist:
        user = User.objects.create_user(username =request.POST['username'],email = request.POST['email'], password = request.POST['password1'])
        login(request, user)
        return render(request, 'accounts/signUp.html')
