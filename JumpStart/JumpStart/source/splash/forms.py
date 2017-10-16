from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class EmailForm(forms.Form):
    attendee_email = forms.EmailField()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

