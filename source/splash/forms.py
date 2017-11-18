from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class EmailForm(forms.Form):
    attendee_email = forms.EmailField()
