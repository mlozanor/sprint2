from django.db import models

from BancoDeLosAlpes.models import BancoDeLosAlpes

class Clientes(models.Model):
    
    banco = models.ForeignKey(BancoDeLosAlpes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nombre

# Create your models here.
