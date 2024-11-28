from django.db import models

# Create your models here.

class Productos(models.Model):
    idProductos=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=1000)
    Precio=models.CharField(max_length=100)
    idCategoria=models.CharField( max_length=6)
    idProvedores=models.CharField(max_length=6)
    Descripcion=models.CharField(max_length=100)
    CantidadStock=models.CharField(max_length=100)

def __str__(self):
        return self.Nombre