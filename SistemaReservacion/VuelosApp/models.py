from django.db import models

# Create your models here.

class Vuelos(models.Model):
    origen=models.CharField(max_length=30)
    destino=models.CharField(max_length=30)
    fechaViaje=models.DateTimeField()
    numAsientos=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='vuelo'
        verbose_name_plural='vuelos'

    def __str__(self):
        return self.origen