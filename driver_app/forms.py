from django import forms
from django.forms import ModelForm
from .models import VehicleInspectionReport
from django.contrib.admin import widgets

class VehicleInspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('date', 'engine_check', 'engine_desc', 'transmission_check',
         'transmission_desc', 'steering_check', 'steering_desc', 'horn_check', 'horn_desc',
         'wipers_check', 'wipers_desc', 'mirrors_check', 'mirrors_desc', 'lights_check', 'lights_type', 'lights_desc',
         'brakes_check', 'brakes_desc', 'air_lines_check', 'air_lines_desc', 'tires_check', 'tires_desc', 
         'wheels_check', 'wheels_desc', 'emergency_check', 'emergency_type', 'emergency_desc', 'coupling_check', 'coupling_desc',
         'other_check', 'other_desc',)

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control" })
        
        self.fields['engine_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "engine_check" })
        self.fields['engine_check'].label = "Engine"
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_desc'].label = ""

        self.fields['transmission_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "transmission_check" })
        self.fields['transmission_check'].label = "Transmission"
        self.fields['transmission_desc'].widget = forms.widgets.Textarea(attrs={'id': "transmission", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['transmission_desc'].label = ""

        self.fields['steering_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "steering_check" })
        self.fields['steering_check'].label = "Steering"
        self.fields['steering_desc'].widget = forms.widgets.Textarea(attrs={'id': "steering", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['steering_desc'].label = ""

        self.fields['horn_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "horn_check" })
        self.fields['horn_check'].label = "Horn"
        self.fields['horn_desc'].widget = forms.widgets.Textarea(attrs={'id': "horn", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['horn_desc'].label = ""

        self.fields['wipers_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wipers_check" })
        self.fields['wipers_check'].label = "Windshield Wipers"
        self.fields['wipers_desc'].widget = forms.widgets.Textarea(attrs={'id': "wipers", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wipers_desc'].label = ""

        self.fields['mirrors_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "mirrors_check" })
        self.fields['mirrors_check'].label = "Mirrors"
        self.fields['mirrors_desc'].widget = forms.widgets.Textarea(attrs={'id': "mirrors", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['mirrors_desc'].label = ""

        self.fields['lights_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "lights_check" })
        self.fields['lights_check'].label = "Lights"
        self.fields['lights_type'].widget.attrs['id'] = 'lights_type'
        self.fields['lights_type'].widget.attrs['class'] = 'form-select'
        self.fields['lights_type'].widget.attrs['style'] = 'display: none'
        self.fields['lights_type'].label = ""
        self.fields['lights_desc'].widget = forms.widgets.Textarea(attrs={'id': "lights", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['lights_desc'].label = ""

        self.fields['brakes_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "brakes_check" })
        self.fields['brakes_check'].label = "Brakes"
        self.fields['brakes_desc'].widget = forms.widgets.Textarea(attrs={'id': "brakes", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['brakes_desc'].label = ""

        self.fields['air_lines_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "air_lines_check" })
        self.fields['air_lines_check'].label = "Air Lines"
        self.fields['air_lines_desc'].widget = forms.widgets.Textarea(attrs={'id': "air_lines", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['air_lines_desc'].label = ""

        self.fields['tires_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "tires_check" })
        self.fields['tires_check'].label = "Tires"
        self.fields['tires_desc'].widget = forms.widgets.Textarea(attrs={'id': "tires", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['tires_desc'].label = ""

        self.fields['wheels_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wheels_check" })
        self.fields['wheels_check'].label = "Wheels"
        self.fields['wheels_desc'].widget = forms.widgets.Textarea(attrs={'id': "wheels", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wheels_desc'].label = ""

        self.fields['emergency_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "emergency_check" })
        self.fields['emergency_check'].label = "Emergency Equipment"
        self.fields['emergency_type'].widget.attrs['id'] = 'emergency_type'
        self.fields['emergency_type'].widget.attrs['class'] = 'form-select'
        self.fields['emergency_type'].widget.attrs['style'] = 'display: none'
        self.fields['emergency_type'].label = ""
        self.fields['emergency_desc'].widget = forms.widgets.Textarea(attrs={'id': "emergency", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['emergency_desc'].label = ""

        self.fields['coupling_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "coupling_check" })
        self.fields['coupling_check'].label = "Coupling"
        self.fields['coupling_desc'].widget = forms.widgets.Textarea(attrs={'id': "coupling", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['coupling_desc'].label = ""

        self.fields['other_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "other_check" })
        self.fields['other_check'].label = "Other"
        self.fields['other_desc'].widget = forms.widgets.Textarea(attrs={'id': "other", 'class': "form-control", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['other_desc'].label = ""





class MechVehicleInspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('date', 'engine_check', 'engine_desc', 'transmission_check',
         'transmission_desc', 'steering_check', 'steering_desc', 'horn_check', 'horn_desc',
         'wipers_check', 'wipers_desc', 'mirrors_check', 'mirrors_desc', 'lights_check', 'lights_type', 'lights_desc',
         'brakes_check', 'brakes_desc', 'air_lines_check', 'air_lines_desc', 'tires_check', 'tires_desc', 
         'wheels_check', 'wheels_desc', 'emergency_check', 'emergency_type', 'emergency_desc', 'coupling_check', 'coupling_desc',
         'other_check', 'other_desc',)

    def __init__(self, *args, **kwargs):
        super(MechVehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control", 'readonly': "readonly" })
        
        self.fields['engine_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "engine_check" })
        self.fields['engine_check'].label = "Engine"
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control ", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_desc'].label = ""

        self.fields['transmission_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "transmission_check" })
        self.fields['transmission_check'].label = "Transmission"
        self.fields['transmission_desc'].widget = forms.widgets.Textarea(attrs={'id': "transmission", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['transmission_desc'].label = ""

        self.fields['steering_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "steering_check" })
        self.fields['steering_check'].label = "Steering"
        self.fields['steering_desc'].widget = forms.widgets.Textarea(attrs={'id': "steering", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['steering_desc'].label = ""

        self.fields['horn_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "horn_check" })
        self.fields['horn_check'].label = "Horn"
        self.fields['horn_desc'].widget = forms.widgets.Textarea(attrs={'id': "horn", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['horn_desc'].label = ""

        self.fields['wipers_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wipers_check" })
        self.fields['wipers_check'].label = "Windshield Wipers"
        self.fields['wipers_desc'].widget = forms.widgets.Textarea(attrs={'id': "wipers", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wipers_desc'].label = ""

        self.fields['mirrors_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "mirrors_check" })
        self.fields['mirrors_check'].label = "Mirrors"
        self.fields['mirrors_desc'].widget = forms.widgets.Textarea(attrs={'id': "mirrors", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['mirrors_desc'].label = ""

        self.fields['lights_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "lights_check" })
        self.fields['lights_check'].label = "Lights"
        self.fields['lights_type'].widget.attrs['id'] = 'lights_type'
        self.fields['lights_type'].widget.attrs['class'] = 'form-select'
        self.fields['lights_type'].widget.attrs['style'] = 'display: none'
        self.fields['lights_type'].label = ""
        self.fields['lights_desc'].widget = forms.widgets.Textarea(attrs={'id': "lights", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['lights_desc'].label = ""

        self.fields['brakes_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "brakes_check" })
        self.fields['brakes_check'].label = "Brakes"
        self.fields['brakes_desc'].widget = forms.widgets.Textarea(attrs={'id': "brakes", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['brakes_desc'].label = ""

        self.fields['air_lines_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "air_lines_check" })
        self.fields['air_lines_check'].label = "Air Lines"
        self.fields['air_lines_desc'].widget = forms.widgets.Textarea(attrs={'id': "air_lines", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['air_lines_desc'].label = ""

        self.fields['tires_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "tires_check" })
        self.fields['tires_check'].label = "Tires"
        self.fields['tires_desc'].widget = forms.widgets.Textarea(attrs={'id': "tires", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['tires_desc'].label = ""

        self.fields['wheels_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wheels_check" })
        self.fields['wheels_check'].label = "Wheels"
        self.fields['wheels_desc'].widget = forms.widgets.Textarea(attrs={'id': "wheels", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wheels_desc'].label = ""

        self.fields['emergency_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "emergency_check" })
        self.fields['emergency_check'].label = "Emergency Equipment"
        self.fields['emergency_type'].widget.attrs['id'] = 'emergency_type'
        self.fields['emergency_type'].widget.attrs['class'] = 'form-select'
        self.fields['emergency_type'].widget.attrs['style'] = 'display: none'
        self.fields['emergency_type'].label = ""
        self.fields['emergency_desc'].widget = forms.widgets.Textarea(attrs={'id': "emergency", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['emergency_desc'].label = ""

        self.fields['coupling_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "coupling_check" })
        self.fields['coupling_check'].label = "Coupling"
        self.fields['coupling_desc'].widget = forms.widgets.Textarea(attrs={'id': "coupling", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['coupling_desc'].label = ""

        self.fields['other_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "other_check" })
        self.fields['other_check'].label = "Other"
        self.fields['other_desc'].widget = forms.widgets.Textarea(attrs={'id': "other", 'class': "form-control", 'readonly': "readonly", 'style': "display: none", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['other_desc'].label = ""


class ReadVehicleinspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('repairStatus', 'date', 'equipment', 'engine_desc', 'engine_fix')

    def __init__(self, *args, **kwargs):
        super(VehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control" })
        self.fields['truck'].widget = forms.widgets.TextInput(attrs={'class': "form-control" })
        #self.fields['repairStatus'].widget = forms.widgets.CheckboxInput(attrs={'class': "d-none" })
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_fix'].widget = forms.widgets.Textarea(attrs={'id': "engine_fix", 'class': "form-control", 'placeholder': "Enter the steps you took for your repair..."})


        self.fields['engine_desc'].label = ""