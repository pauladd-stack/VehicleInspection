# Generated by Django 3.2.9 on 2022-01-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0007_auto_20220119_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinspectionreport',
            name='lastUpdatedMech',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleinspectionreport',
            name='lastUpdatedUser',
            field=models.DateField(blank=True, null=True),
        ),
    ]
