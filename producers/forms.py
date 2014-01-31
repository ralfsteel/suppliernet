from django import forms
from django.contrib.auth.models import User

from producers.models import Client





class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Client
        fields = ['name', 'password', 'address', 'zipcode', 'city', 'phone', 'phones', 'fax', 'email']


class LoginForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())

     class Meta:
         model = Client
         fields = ['name', 'password']




