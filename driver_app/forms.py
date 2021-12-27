from django import forms
from django.forms import ModelForm
from .models import VehicleInspectionReport
from django.contrib.admin import widgets                                       


class VehicleInspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('date', 'truck')

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date', 'class': "form-control" })
        self.fields['truck'].widget = forms.widgets.TextInput(attrs={'class': "form-control" })