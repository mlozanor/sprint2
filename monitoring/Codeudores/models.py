from django.db import models


class Codeudores(models.Model):

    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre


# Create your models here.
