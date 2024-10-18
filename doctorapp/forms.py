
from django import forms
from .models import *

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ['tip_text']


