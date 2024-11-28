from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.CharField(verbose_name="idCategoria",primary_key=True,max_length=6)
    Nombre=models.CharField(verbose_name="Nombre",max_length=1000)
    idProducto=models.CharField(verbose_name="idProducto",max_length=100)
    Promociones=models.CharField(max_length=100)
    Tamaño=models.CharField(verbose_name="Tamaño",max_length=100)
    Color=models.CharField(verbose_name="Color",max_length=100)
    Genero=models.CharField(verbose_name="Genero",max_length=100)

def __str__(self):
        return self.Nombre