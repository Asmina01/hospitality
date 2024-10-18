from django.conf import settings
from django.contrib.auth.models import User
from django.db import models



class Facility(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='facility_images/', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.name

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Doctor_hospital(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Doc_name = models.CharField(max_length=200)
    Doc_department = models.CharField(max_length=200)
    images = models.ImageField(blank=True, null=True, upload_to='doctor_images/')

    def __str__(self):
        return self.Doc_name