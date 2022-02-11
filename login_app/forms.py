from django.forms import ModelForm
from user_app.models import User

class LoginForm(ModelForm):
        class Meta:
                model = User
                fields = ["email", "password"]