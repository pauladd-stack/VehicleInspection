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
        fields = ('date', 'engine_check', 'engine_desc', 'engine_fix', 'transmission_check',
         'transmission_desc', 'transmission_fix', 'steering_check', 'steering_desc', 'steering_fix', 'horn_check', 'horn_desc', 'horn_fix',
         'wipers_check', 'wipers_desc', 'wipers_fix', 'mirrors_check', 'mirrors_desc', 'mirrors_fix', 'lights_check', 'lights_type', 'lights_desc', 'lights_fix',
         'brakes_check', 'brakes_desc', 'brakes_fix', 'air_lines_check', 'air_lines_desc', 'air_lines_fix', 'tires_check', 'tires_desc', 'tires_fix',
         'wheels_check', 'wheels_desc', 'wheels_fix', 'emergency_check', 'emergency_type', 'emergency_desc', 'emergency_fix', 'coupling_check', 'coupling_desc', 'coupling_fix',
         'other_check', 'other_desc', 'other_fix')

    def __init__(self, *args, **kwargs):
        super(MechVehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control", 'readonly': "readonly" })
        
        self.fields['engine_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "engine_check", 'style': "display: none"})
        self.fields['engine_check'].label = "Engine"
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control ", 'readonly': "readonly",'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_desc'].label = ""
        self.fields['engine_fix'].widget = forms.widgets.Textarea(attrs={'id': "engine_fix", 'class': "form-control ",'placeholder': "Describe how you fixed the issue..."})


        self.fields['transmission_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "transmission_check", 'style': "display: none"})
        self.fields['transmission_check'].label = "Transmission"
        self.fields['transmission_desc'].widget = forms.widgets.Textarea(attrs={'id': "transmission", 'class': "form-control", 'readonly': "readonly",'placeholder': "Enter a description of the issue you are having..."})
        self.fields['transmission_desc'].label = ""
        self.fields['transmission_fix'].widget = forms.widgets.Textarea(attrs={'id': "transmission_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['steering_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "steering_check", 'style': "display: none"})
        self.fields['steering_check'].label = "Steering"
        self.fields['steering_desc'].widget = forms.widgets.Textarea(attrs={'id': "steering", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['steering_desc'].label = ""
        self.fields['steering_fix'].widget = forms.widgets.Textarea(attrs={'id': "steering_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['horn_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "horn_check", 'style': "display: none"})
        self.fields['horn_check'].label = "Horn"
        self.fields['horn_desc'].widget = forms.widgets.Textarea(attrs={'id': "horn", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['horn_desc'].label = ""
        self.fields['horn_fix'].widget = forms.widgets.Textarea(attrs={'id': "horn_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['wipers_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wipers_check", 'style': "display: none"})
        self.fields['wipers_check'].label = "Windshield Wipers"
        self.fields['wipers_desc'].widget = forms.widgets.Textarea(attrs={'id': "wipers", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wipers_desc'].label = ""
        self.fields['wipers_fix'].widget = forms.widgets.Textarea(attrs={'id': "wipers_fix", 'class': "form-control ",  'placeholder': "Describe how you fixed the issue..."})


        self.fields['mirrors_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "mirrors_check", 'style': "display: none"})
        self.fields['mirrors_check'].label = "Mirrors"
        self.fields['mirrors_desc'].widget = forms.widgets.Textarea(attrs={'id': "mirrors", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['mirrors_desc'].label = ""
        self.fields['mirrors_fix'].widget = forms.widgets.Textarea(attrs={'id': "mirrors_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['lights_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "lights_check", 'style': "display: none"})
        self.fields['lights_check'].label = "Lights"
        self.fields['lights_type'].widget.attrs['id'] = 'lights_type'
        self.fields['lights_type'].widget.attrs['class'] = 'form-control'
        self.fields['lights_type'].widget.attrs['readonly'] = 'readonly'
        self.fields['lights_type'].widget.attrs['style'] = 'pointer-events: none'
        self.fields['lights_type'].label = ""
        self.fields['lights_desc'].widget = forms.widgets.Textarea(attrs={'id': "lights", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['lights_desc'].label = ""
        self.fields['lights_fix'].widget = forms.widgets.Textarea(attrs={'id': "lights_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['brakes_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "brakes_check", 'style': "display: none"})
        self.fields['brakes_check'].label = "Brakes"
        self.fields['brakes_desc'].widget = forms.widgets.Textarea(attrs={'id': "brakes", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['brakes_desc'].label = ""
        self.fields['brakes_fix'].widget = forms.widgets.Textarea(attrs={'id': "brakes_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['air_lines_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "air_lines_check", 'style': "display: none"})
        self.fields['air_lines_check'].label = "Air Lines"
        self.fields['air_lines_desc'].widget = forms.widgets.Textarea(attrs={'id': "air_lines", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['air_lines_desc'].label = ""
        self.fields['air_lines_fix'].widget = forms.widgets.Textarea(attrs={'id': "air_lines_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['tires_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "tires_check", 'style': "display: none"})
        self.fields['tires_check'].label = "Tires"
        self.fields['tires_desc'].widget = forms.widgets.Textarea(attrs={'id': "tires", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['tires_desc'].label = ""
        self.fields['tires_fix'].widget = forms.widgets.Textarea(attrs={'id': "tires_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['wheels_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wheels_check", 'style': "display: none"})
        self.fields['wheels_check'].label = "Wheels"
        self.fields['wheels_desc'].widget = forms.widgets.Textarea(attrs={'id': "wheels", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wheels_desc'].label = ""
        self.fields['wheels_fix'].widget = forms.widgets.Textarea(attrs={'id': "wheels_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['emergency_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "emergency_check", 'style': "display: none"})
        self.fields['emergency_check'].label = "Emergency Equipment"
        self.fields['emergency_type'].widget.attrs['id'] = 'emergency_type'
        self.fields['emergency_type'].widget.attrs['class'] = 'form-control'
        self.fields['emergency_type'].widget.attrs['readonly'] = 'readonly'
        self.fields['emergency_type'].widget.attrs['style'] = 'pointer-events: none'
        self.fields['emergency_type'].label = ""
        self.fields['emergency_desc'].widget = forms.widgets.Textarea(attrs={'id': "emergency", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['emergency_desc'].label = ""
        self.fields['emergency_fix'].widget = forms.widgets.Textarea(attrs={'id': "emergency_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['coupling_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "coupling_check", 'style': "display: none"})
        self.fields['coupling_check'].label = "Coupling"
        self.fields['coupling_desc'].widget = forms.widgets.Textarea(attrs={'id': "coupling", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['coupling_desc'].label = ""
        self.fields['coupling_fix'].widget = forms.widgets.Textarea(attrs={'id': "coupling_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['other_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "other_check", 'style': "display: none"})
        self.fields['other_check'].label = "Other"
        self.fields['other_desc'].widget = forms.widgets.Textarea(attrs={'id': "other", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['other_desc'].label = ""
        self.fields['other_fix'].widget = forms.widgets.Textarea(attrs={'id': "other_fix", 'class': "form-control ", 'placeholder': "Describe how you fixed the issue..."})


class ReadVehicleInspectionForm(ModelForm):

    class Meta:
        model = VehicleInspectionReport
        fields = ('date', 'engine_check', 'engine_desc', 'engine_fix', 'transmission_check',
         'transmission_desc', 'transmission_fix', 'steering_check', 'steering_desc', 'steering_fix', 'horn_check', 'horn_desc', 'horn_fix',
         'wipers_check', 'wipers_desc', 'wipers_fix', 'mirrors_check', 'mirrors_desc', 'mirrors_fix', 'lights_check', 'lights_type', 'lights_desc', 'lights_fix',
         'brakes_check', 'brakes_desc', 'brakes_fix', 'air_lines_check', 'air_lines_desc', 'air_lines_fix', 'tires_check', 'tires_desc', 'tires_fix',
         'wheels_check', 'wheels_desc', 'wheels_fix', 'emergency_check', 'emergency_type', 'emergency_desc', 'emergency_fix', 'coupling_check', 'coupling_desc', 'coupling_fix',
         'other_check', 'other_desc', 'other_fix')

    def __init__(self, *args, **kwargs):
        super(ReadVehicleInspectionForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(attrs={'type': "date", 'class': "form-control", 'readonly': "readonly" })
        
        self.fields['engine_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "engine_check", 'style': "display: none"})
        self.fields['engine_check'].label = "Engine"
        self.fields['engine_desc'].widget = forms.widgets.Textarea(attrs={'id': "engine", 'class': "form-control ", 'readonly': "readonly",'placeholder': "Enter a description of the issue you are having..."})
        self.fields['engine_desc'].label = ""
        self.fields['engine_fix'].widget = forms.widgets.Textarea(attrs={'id': "engine_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})


        self.fields['transmission_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "transmission_check", 'style': "display: none"})
        self.fields['transmission_check'].label = "Transmission"
        self.fields['transmission_desc'].widget = forms.widgets.Textarea(attrs={'id': "transmission", 'class': "form-control", 'readonly': "readonly",'placeholder': "Enter a description of the issue you are having..."})
        self.fields['transmission_desc'].label = ""
        self.fields['transmission_fix'].widget = forms.widgets.Textarea(attrs={'id': "transmission_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['steering_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "steering_check", 'style': "display: none"})
        self.fields['steering_check'].label = "Steering"
        self.fields['steering_desc'].widget = forms.widgets.Textarea(attrs={'id': "steering", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['steering_desc'].label = ""
        self.fields['steering_fix'].widget = forms.widgets.Textarea(attrs={'id': "steering_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['horn_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "horn_check", 'style': "display: none"})
        self.fields['horn_check'].label = "Horn"
        self.fields['horn_desc'].widget = forms.widgets.Textarea(attrs={'id': "horn", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['horn_desc'].label = ""
        self.fields['horn_fix'].widget = forms.widgets.Textarea(attrs={'id': "horn_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['wipers_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wipers_check", 'style': "display: none"})
        self.fields['wipers_check'].label = "Windshield Wipers"
        self.fields['wipers_desc'].widget = forms.widgets.Textarea(attrs={'id': "wipers", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wipers_desc'].label = ""
        self.fields['wipers_fix'].widget = forms.widgets.Textarea(attrs={'id': "wipers_fix", 'class': "form-control ", 'readonly': "readonly",  'placeholder': "Describe how you fixed the issue..."})


        self.fields['mirrors_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "mirrors_check", 'style': "display: none"})
        self.fields['mirrors_check'].label = "Mirrors"
        self.fields['mirrors_desc'].widget = forms.widgets.Textarea(attrs={'id': "mirrors", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['mirrors_desc'].label = ""
        self.fields['mirrors_fix'].widget = forms.widgets.Textarea(attrs={'id': "mirrors_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['lights_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "lights_check", 'style': "display: none"})
        self.fields['lights_check'].label = "Lights"
        self.fields['lights_type'].widget.attrs['id'] = 'lights_type'
        self.fields['lights_type'].widget.attrs['class'] = 'form-control'
        self.fields['lights_type'].widget.attrs['readonly'] = 'readonly'
        self.fields['lights_type'].widget.attrs['style'] = 'pointer-events: none'
        self.fields['lights_type'].label = ""
        self.fields['lights_desc'].widget = forms.widgets.Textarea(attrs={'id': "lights", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['lights_desc'].label = ""
        self.fields['lights_fix'].widget = forms.widgets.Textarea(attrs={'id': "lights_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['brakes_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "brakes_check", 'style': "display: none"})
        self.fields['brakes_check'].label = "Brakes"
        self.fields['brakes_desc'].widget = forms.widgets.Textarea(attrs={'id': "brakes", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['brakes_desc'].label = ""
        self.fields['brakes_fix'].widget = forms.widgets.Textarea(attrs={'id': "brakes_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['air_lines_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "air_lines_check", 'style': "display: none"})
        self.fields['air_lines_check'].label = "Air Lines"
        self.fields['air_lines_desc'].widget = forms.widgets.Textarea(attrs={'id': "air_lines", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['air_lines_desc'].label = ""
        self.fields['air_lines_fix'].widget = forms.widgets.Textarea(attrs={'id': "air_lines_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['tires_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "tires_check", 'style': "display: none"})
        self.fields['tires_check'].label = "Tires"
        self.fields['tires_desc'].widget = forms.widgets.Textarea(attrs={'id': "tires", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['tires_desc'].label = ""
        self.fields['tires_fix'].widget = forms.widgets.Textarea(attrs={'id': "tires_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['wheels_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "wheels_check", 'style': "display: none"})
        self.fields['wheels_check'].label = "Wheels"
        self.fields['wheels_desc'].widget = forms.widgets.Textarea(attrs={'id': "wheels", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['wheels_desc'].label = ""
        self.fields['wheels_fix'].widget = forms.widgets.Textarea(attrs={'id': "wheels_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['emergency_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "emergency_check", 'style': "display: none"})
        self.fields['emergency_check'].label = "Emergency Equipment"
        self.fields['emergency_type'].widget.attrs['id'] = 'emergency_type'
        self.fields['emergency_type'].widget.attrs['class'] = 'form-control'
        self.fields['emergency_type'].widget.attrs['readonly'] = 'readonly'
        self.fields['emergency_type'].widget.attrs['style'] = 'pointer-events: none'
        self.fields['emergency_type'].label = ""
        self.fields['emergency_desc'].widget = forms.widgets.Textarea(attrs={'id': "emergency", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['emergency_desc'].label = ""
        self.fields['emergency_fix'].widget = forms.widgets.Textarea(attrs={'id': "emergency_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['coupling_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "coupling_check", 'style': "display: none"})
        self.fields['coupling_check'].label = "Coupling"
        self.fields['coupling_desc'].widget = forms.widgets.Textarea(attrs={'id': "coupling", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['coupling_desc'].label = ""
        self.fields['coupling_fix'].widget = forms.widgets.Textarea(attrs={'id': "coupling_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

        self.fields['other_check'].widget = forms.widgets.CheckboxInput(attrs={'id': "other_check", 'style': "display: none"})
        self.fields['other_check'].label = "Other"
        self.fields['other_desc'].widget = forms.widgets.Textarea(attrs={'id': "other", 'class': "form-control", 'readonly': "readonly", 'placeholder': "Enter a description of the issue you are having..."})
        self.fields['other_desc'].label = ""
        self.fields['other_fix'].widget = forms.widgets.Textarea(attrs={'id': "other_fix", 'class': "form-control ", 'readonly': "readonly", 'placeholder': "Describe how you fixed the issue..."})

