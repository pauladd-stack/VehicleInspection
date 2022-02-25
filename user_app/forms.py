from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

'''
class RegisterForm(forms.ModelForm):

    The default 



    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email',]

    def clean_email(self):

        #Verify email is available.

        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):

        #Verify both passwords match.

        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

'''

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role']

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})
        self.fields['last_name'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})
        self.fields['role'].widget.attrs['class'] = 'form-select'

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    #password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'is_active', 'admin']

    def __init__(self, *args, **kwargs):
        super(UserAdminChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})
        self.fields['last_name'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})
        self.fields['email'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})
        self.fields['role'].widget.attrs['class'] = 'form-select'

    #def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        #return self.initial["password"]




class ProfileUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(ProfileUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})
        self.fields['last_name'].widget = forms.widgets.TextInput(attrs={'class': "form-control"})


class ProfilePasswordChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'onfocus': "this.value=''", 'value': "**************", 'placeholder': "Enter a password..."}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'onfocus': "this.value=''", 'value': "***0*****9****", 'placeholder': "Re-enter password..."}))
    

    class Meta:
        model = User
        fields = []

    def __init__(self, *args, **kwargs):
        super(ProfilePasswordChangeForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user