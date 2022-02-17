from django.forms import ModelForm
from user_app.models import User
from django import forms
from django.contrib.admin import widgets


class LoginForm(ModelForm):
        class Meta:
                model = User
                fields = ["email", "password"]

        def __init__(self, *args, **kwargs):
                super(LoginForm, self).__init__(*args, **kwargs)
                self.fields['email'].widget = forms.widgets.EmailInput(attrs={'class': "form-control" })
                self.fields['password'].widget = forms.widgets.PasswordInput(attrs={'class': "form-control"})