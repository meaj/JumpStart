from django import forms
from importing.models import csv_file

class CSV_Form(forms.ModelForm):
    class Meta:
        model = csv_file
        fields = ('description', 'document',)