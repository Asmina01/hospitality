# Generated by Django 4.2.14 on 2024-10-15 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0002_prescription_patient_prescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_prescription',
            old_name='Status',
            new_name='status',
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]