
from django import forms

from django.contrib.auth.forms import UserCreationForm

from hospitalapp.models import *
class Doctorform(forms.ModelForm):

    class Meta:

        model=Doctor_hospital
        fields="__all__"


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'description', 'image', 'status']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class DoctorRegistrationForm(forms.ModelForm):
    doc_username = forms.CharField(max_length=150, label="Doctor Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = Doctor_hospital
        fields = ['Doc_name', 'Doc_department', 'images']

    def clean_doc_username(self):
        username = self.cleaned_data.get('doc_username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another.")
        return username




