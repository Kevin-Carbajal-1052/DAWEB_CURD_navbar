from django.db import models

# Create your models here.

class Empleados(models.Model):
    idEmpleados=models.IntegerField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=1000)
    Telefono=models.IntegerField(null=False, blank=False, max_length=15)
    Direccion=models.CharField(max_length=100)
    Correo=models.CharField(null=False, blank=False,max_length=100)
    Turno=models.CharField(max_length=100)
    Sueldo=models.IntegerField(max_length=100)
    Puesto=models.CharField(max_length=100)

def __str__(self):
        return self.Nombre