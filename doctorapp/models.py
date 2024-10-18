
from django.db import models
from userapp.models import Doc_appointment

class Health(models.Model):

    tip_text=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Patient_prescription(models.Model):
    Appointment = models.OneToOneField(Doc_appointment, on_delete=models.CASCADE)
    Prescription = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"Prescription for {self.Appointment} - Status: {self.status}"





