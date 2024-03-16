from django.db import models

from BancoDeLosAlpes.models import BancoDeLosAlpes

class Prospectos(models.Model):
    
    banco = models.ForeignKey(BancoDeLosAlpes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nombre

