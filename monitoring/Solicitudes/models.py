from django.db import models

from Clientes.models import Clientes
from Empleados.models import Empleados
from Codeudores.models import Codeudores

class Solicitudes(models.Model):

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empleado = models.ManyToManyField(Empleados)
    codeudor = models.ForeignKey(Codeudores, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    
    def __str__(self):
        return self.cliente.nombre
