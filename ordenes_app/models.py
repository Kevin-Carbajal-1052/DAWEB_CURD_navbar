from django.db import models

# Create your models here.

class Ordenes(models.Model):
    idOrdenes=models.CharField(verbose_name="idOrdenes",primary_key=True,max_length=6)
    idClientes=models.CharField(verbose_name="idClientes",max_length=1000)
    FechaOrden=models.DateField(verbose_name="Fecha de orden", null=False, blank=False)
    Cantidad=models.CharField(max_length=100)
    FechaEnvio=models.DateField(verbose_name="Fecha de envio", null=False, blank=False)
    DireccionEnvio=models.CharField(verbose_name="Direccion de envio",max_length=100)
    idEmpleado=models.CharField(verbose_name="idEmpleado",max_length=100)
    idProducto=models.CharField(verbose_name="idProductos",max_length=100)

def __str__(self):
        return self.idClientes