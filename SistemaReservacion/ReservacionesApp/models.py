from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adultos = models.IntegerField()
    niños = models.IntegerField()
    nombre = models.CharField(max_length=50)
    paisOrigen = models.CharField(max_length=30,
    choices=COUNTRIES)
    fechaNacimiento = models.DateField()
    class Meta:
        verbose_name='reserva'
        verbose_name_plural='reservas'

    def __str__(self):
        return self.nombre

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