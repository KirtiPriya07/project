from django import forms
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import MyUser
from crispy_forms.helper import FormHelper

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = PhoneField(blank=True)
    address = forms.CharField(label="address", max_length=200)
    name = forms.CharField(label="name", max_length=100)
    class Meta:
        model = MyUser
        helper = FormHelper()
        helper.exclude = ['password']
        fields = ['name', 'email', 'phone_number', 'address']