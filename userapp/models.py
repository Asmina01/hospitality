from django.db import models

from django.contrib.auth.models import User
from hospitalapp.models import Doctor_hospital




class Doc_appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor_hospital, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(blank=True, null=True)

def __str__(self):
        return f"Appointment with {self.doctor} on {self.date} at {self.time} "

class patient_Payment(models.Model):
    appointment = models.OneToOneField('Doc_appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

