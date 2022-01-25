from django import forms
from django.forms import ModelForm
from .models import VehicleInspectionReport
from django.contrib.admin import widgets                                       


class VehicleInspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('repairStatus', 'date', 'truck', 'engine_check', 'engine_desc')

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control" })
        self.fields['truck'].widget = forms.widgets.TextInput(attrs={'class': "form-control" })
        self.fields['repairStatus'].widget = forms.widgets.CheckboxInput(attrs={'class': "d-none" })
        self.fields['engine_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "engine_check" })
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control", 'placeholder': "Enter a description of the issue you are having..."})

        self.fields['engine_desc'].label = ""


class MechVehicleinspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('repairStatus', 'date', 'truck', 'engine_desc', 'engine_fix')

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control" })
        self.fields['truck'].widget = forms.widgets.TextInput(attrs={'class': "form-control" })
        self.fields['repairStatus'].widget = forms.widgets.CheckboxInput(attrs={'class': "d-none" })
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_fix'].widget = forms.widgets.Textarea(attrs={'id': "engine_fix", 'class': "form-control", 'placeholder': "Enter the steps you took for your repair..."})


        self.fields['engine_desc'].label = ""


class ReadVehicleinspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('repairStatus', 'date', 'truck', 'engine_desc', 'engine_fix')

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control" })
        self.fields['truck'].widget = forms.widgets.TextInput(attrs={'class': "form-control" })
        #self.fields['repairStatus'].widget = forms.widgets.CheckboxInput(attrs={'class': "d-none" })
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_fix'].widget = forms.widgets.Textarea(attrs={'id': "engine_fix", 'class': "form-control", 'placeholder': "Enter the steps you took for your repair..."})


        self.fields['engine_desc'].label = ""