from django import forms
from first_app.models import LoginModel
from django.core import validators

def check_password(value):
    if value !="abcd":
        raise forms.ValidationError("Invalid Password")


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget = forms.PasswordInput,validators=[check_password,])

    class Meta:
        model = LoginModel
        fields = '__all__'
