from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from ReservacionesApp.models import Reservar

TYPE_PAY = [
    ('transferencia', 'Transeferencia Bancaria'),
    ('tarjeta', 'Tarjeta de Credito'),
]
# Create your models here.

class Pagar(models.Model):
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    reservacion = models.OneToOneField(Reservar, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=30)
    name_prop = models.CharField(max_length=30)
    num_card = models.CharField(max_length=19)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_prop

#class cliente(models.Model):

class PagarForm(ModelForm):
    class Meta:
        model = Pagar
        fields = [
            'tipo_pago',
            'name_prop',
            'num_card'
        ]
        widgets = {
            'tipo_pago': forms.RadioSelect(choices=TYPE_PAY,attrs={'class':'form-control mr-3'} ),
            'name_prop':forms.TextInput(attrs={'class':'form-control mr-3'}),
            'num_card':forms.TextInput(attrs={'class':'form-control mr-3'})
        }