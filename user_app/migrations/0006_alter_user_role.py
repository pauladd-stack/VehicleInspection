# Generated by Django 3.2.9 on 2022-02-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20220211_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Driver', 'Driver'), ('Mechanic', 'Mechanic')], default='Driver', max_length=8),
        ),
    ]
