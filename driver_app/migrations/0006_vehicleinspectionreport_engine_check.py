# Generated by Django 3.2.9 on 2022-01-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0005_rename_enginge_fix_vehicleinspectionreport_engine_fix'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleinspectionreport',
            name='engine_check',
            field=models.BooleanField(default=False),
        ),
    ]
