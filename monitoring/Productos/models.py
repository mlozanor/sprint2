from django.db import models

from BancoDeLosAlpes.models import BancoDeLosAlpes

from Solicitudes.models import Solicitudes

class Productos(models.Model):
        
        banco = models.ForeignKey(BancoDeLosAlpes, on_delete=models.CASCADE)
        solicitud = models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
        tipo = models.CharField(max_length=100)
        descripcion = models.CharField(max_length=100)
        cupo = models.DecimalField(max_digits=10, decimal_places=2)
        
        def __str__(self):
            return self.nombre
