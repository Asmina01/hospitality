
from .models import *
from django import forms


class appointmentform(forms.ModelForm):
    class Meta:
        model = Doc_appointment
        fields = '__all__'

        widgets = {

            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
        }

