# Generated by Django 4.2.14 on 2024-10-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_doctor_hospital'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_appointment',
            name='symptoms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doc_appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.doctor_hospital'),
        ),
    ]