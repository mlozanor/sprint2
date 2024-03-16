from django.db import models

from Solicitudes.models import Solicitudes
from Clientes.models import Clientes

class Documentos(models.Model):
    
        solicitud = models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
        cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
        tipo = models.CharField(max_length=100)
        nombre = models.CharField(max_length=100)
        fecha = models.DateField()
        
        def __str__(self):
            return self.nombre

# Create your models here.
