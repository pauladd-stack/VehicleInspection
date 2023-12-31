# Generated by Django 3.2.9 on 2021-12-21 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleInspectionReport',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('truck', models.CharField(max_length=120, verbose_name='Truck Number')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
