from django import forms
from workshops.models import session

class Session_Form(forms.ModelForm):
    class Meta:
        model = session
        fields = ('session_title','session_date', 'session_location','session_threshold','workshop')