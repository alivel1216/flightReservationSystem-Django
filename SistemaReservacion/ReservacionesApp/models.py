from django.db import models
from django import forms
from django.forms import ModelForm, IntegerField

# Create your models here.

COUNTRIES = [
    ('Alemania', 'Alemania'),
    ('Canadá', 'Canadá'),
    ('Mexico', 'Mexico'),
    ('Colombia', 'Colombia'),
    ('Argentina', 'Argentina'),
    ('Brasil', 'Brasil'),
    ('Peru', 'Peru'),
    ('Ecuador', 'Ecuador'),
    ('Costa Rica', 'Costa Rica'),
    ('Estado Unidos', 'Estado Unidos'),
    ('España', 'España'),
]


class Reservar(models.Model):
    adultos = models.IntegerField()
    niños = models.IntegerField()
    nombre = models.CharField(max_length=50)
    paisOrigen = models.CharField(max_length=30,
    choices=COUNTRIES)
    fechaNacimiento = models.DateField()

class ReservarForm(ModelForm):
    class Meta:
        model = Reservar
        fields = ['adultos',
        'niños',
        'nombre',
        'paisOrigen',
        'fechaNacimiento' ]

        widgets = {'adultos': forms.TextInput(attrs={'class':'form-control mr-3', 'type': 'number'}),
        'niños': forms.TextInput(attrs={'class':'form-control mr-3', 'type': 'number'}),
        'nombre': forms.TextInput(attrs={'class':'form-control mr-3'}),
        #'paisOrigen': forms.TextInput(attrs={'class':' mr-3'}),
        'fechaNacimiento': forms.TextInput(attrs={'class':'form-control mr-3', 'type': 'date'}) }