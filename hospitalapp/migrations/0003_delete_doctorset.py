# Generated by Django 4.2.14 on 2024-10-15 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_doc_appointment_symptoms_and_more'),
        ('hospitalapp', '0002_doctor_hospital'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctorset',
        ),
    ]
