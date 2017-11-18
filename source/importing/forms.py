from django import forms
from importing.models import csv_file, email_template


class CSV_Form(forms.ModelForm):
    class Meta:
        model = csv_file
        fields = ('document',)

    group = forms.CharField(max_length=16)


class Email_Template_Form(forms.ModelForm):
    class Meta:
        model = email_template
        fields = ('email_name', 'email_subject', 'email_body', 'email_signature')
