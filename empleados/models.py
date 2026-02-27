from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre