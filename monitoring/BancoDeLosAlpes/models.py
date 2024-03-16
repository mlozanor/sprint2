from django.db import models

class BancoDeLosAlpes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
