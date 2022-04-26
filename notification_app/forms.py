from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from .models import BroadcastNotification


class NotificationForm(ModelForm):
        class Meta:
                model = BroadcastNotification
                fields = ["message", "date", "driver"]

