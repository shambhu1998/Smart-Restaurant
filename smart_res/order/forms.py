from django import forms
from order.models import LoginModel
from django.core import validators
from django.core.validators import MinValueValidator,MaxValueValidator

def check_password(value):
    if value != 'onetofour':
        raise forms.ValidationError("Invalid Password")

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=128)
    Table_number = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)])
    password = forms.CharField(widget = forms.PasswordInput,validators=[check_password,])

    class Meta:
        model = LoginModel
        fields = '__all__'
