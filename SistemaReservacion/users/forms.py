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
            'username': forms.TextInput(attrs={ 'type':'text'}),
            'first_name': forms.TextInput(attrs={ 'type':'text'}),
            'last_name': forms.TextInput(attrs={ 'type':'text'}),
            'email': forms.TextInput(attrs={'type':'email'}),
            'password1': forms.TextInput(attrs={'type':'password'}),
            'password2': forms.TextInput(attrs={'type':'password'})
        }
        #widgets = {
        #    'username': forms.TextInput(attrs={'class':'zmdi zmdi-account', 'type':'text'}),
        #    'first_name': forms.TextInput(attrs={'class':'zmdi zmdi-account', 'type':'text'}),
        #    'last_name': forms.TextInput(attrs={'class':'zmdi zmdi-account', 'type':'text'}),
        #    'email': forms.TextInput(attrs={'class':'zmdi zmdi-email', 'type':'email'}),
        #    'password1': forms.TextInput(attrs={'class':'zmdi zmdi-lock', 'type':'password'}),
        #    'password2': forms.TextInput(attrs={'class':'zmdi zmdi-lock-outline', 'type':'password'})
        #}