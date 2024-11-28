from django.db import models

# Create your models here.

class Proveedor(models.Model):
    idProveedor = models.IntegerField(verbose_name="idProveedor", primary_key=True, max_length=6)
    Nombre = models.CharField(verbose_name="Nombre", max_length=1000)
    Telefono = models.IntegerField(verbose_name="Telefono", max_length=100)
    Correo = models.EmailField(verbose_name="Correo", max_length=100)
    Direccion = models.CharField(verbose_name="Direccion", max_length=100)
    TipoProducto = models.CharField(verbose_name="Tipo de producto", max_length=100)

    def __str__(self):
        return self.Nombre