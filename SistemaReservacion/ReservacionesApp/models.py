from django.db import models

# Create your models here.


class Reservar(models.Model):
    adultos = models.IntegerField()
    niños = models.IntegerField()
    nombre = models.CharField(max_length=50)


    paisOrigen = {
        ('Ecuador', 'Ecuador'),
        ('Colombia', 'Colombia'),
        ('Peru', 'Peru'),
    }
    fechaNacimiento = models.DateTimeField()
