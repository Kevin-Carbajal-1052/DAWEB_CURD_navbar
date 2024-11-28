from django.db import models

# Create your models here.

class Clientes(models.Model):
    idClientes = models.CharField(verbose_name="idClientes", primary_key=True, max_length=1000)
    Nombre = models.CharField(verbose_name="Nombre", max_length=1000)
    Telefono = models.CharField(verbose_name="Telefono", max_length=100)
    Direccion = models.CharField(verbose_name="Direccion", max_length=1000)
    Correo = models.EmailField(verbose_name="Correo", max_length=1000)
    FechaRegistro = models.DateField(verbose_name="Fecha de registro", null=False, blank=False)

    def __str__(self):
        return self.Nombre