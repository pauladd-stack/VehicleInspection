# Generated by Django 3.2.9 on 2022-02-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_app', '0001_initial'),
        ('driver_app', '0014_historicalvehicleinspectionreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalvehicleinspectionreport',
            name='truck',
        ),
        migrations.RemoveField(
            model_name='vehicleinspectionreport',
            name='truck',
        ),
        migrations.AddField(
            model_name='vehicleinspectionreport',
            name='equipment',
            field=models.ManyToManyField(blank=True, to='equipment_app.Equipment'),
        ),
    ]
