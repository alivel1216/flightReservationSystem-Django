from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createdUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={ 'class':'form-group  ','type':'text', 'placeholder':'Nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'class':'form-group  ', 'type':'text'}),
            'last_name': forms.TextInput(attrs={'class':'form-group  ', 'type':'text'}),
            'email': forms.TextInput(attrs={'class':'form-group  ','type':'email'}),
            'password1': forms.TextInput(attrs={'class':'form-group  ','type':'password'}),
            'password2': forms.TextInput(attrs={'class':'form-group  ','type':'password'})
        }