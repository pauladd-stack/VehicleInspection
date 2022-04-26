from django import forms
from django.forms import ModelForm
from .models import Equipment
from django.contrib.admin import widgets

class DriverChangeForm(ModelForm):

    class Meta:
        model = Equipment
        fields = ('driver',)

    def __init__(self, *args, **kwargs):
        super(DriverChangeForm, self).__init__(*args, **kwargs)
        self.fields['driver'].widget.attrs['id'] = 'driver'
        self.fields['driver'].widget.attrs['class'] = 'form-select'
        self.fields['driver'].required=False
        self.fields['driver'].label = ""