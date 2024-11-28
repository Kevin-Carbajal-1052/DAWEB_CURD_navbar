from django.shortcuts import render,redirect
from .models import Empleados
# Create your views here.
def inicio_vistaEmpleados(request):
    lasEmpleados=Empleados.objects.all()
    return render(request, 'gestionarEmpleados.html',{'misEmpleados':lasEmpleados})

def registrarEmpleados(request):
    idEmpleados=request.POST["idEmpleados"]
    Nombre=request.POST["Nombre"]
    Telefono=request.POST["Telefono"]
    Direccion=request.POST["Direccion"]
    Correo=request.POST["Correo"]
    Turno=request.POST["Turno"]
    Sueldo=request.POST["Sueldo"]
    Puesto=request.POST["Puesto"]
    guardarEmpleado=Empleados.objects.create(idEmpleados=idEmpleados,Nombre=Nombre,Telefono=Telefono,Direccion=Direccion,Correo=Correo,Turno=Turno,Sueldo=Sueldo,Puesto=Puesto)
    return redirect('empleados')

def seleccionarEmpleados(request,idEmpleados):
    empleado=Empleados.objects.get(idEmpleados=idEmpleados)
    return render(request,"editarEmpleados.html",{"misEmpleados":empleado})

def editarEmpleado(request):
    idEmpleados=request.POST["idEmpleados"]
    Nombre=request.POST["Nombre"]
    Telefono=request.POST["Telefono"]
    Direccion=request.POST["Direccion"]
    Correo=request.POST["Correo"]
    Turno=request.POST["Turno"]
    Sueldo=request.POST["Sueldo"]
    Puesto=request.POST["Puesto"]
    empleado=Empleados.objects.get(idEmpleados=idEmpleados)
    empleado.idEmpleados=idEmpleados
    empleado.Nombre=Nombre
    empleado.Telefono=Telefono
    empleado.Direccion=Direccion
    empleado.Correo=Correo
    empleado.Turno=Turno
    empleado.Sueldo=Sueldo
    empleado.Puesto=Puesto
    empleado.save()
    return redirect('empleados')

def borrarEmpleado(request,idEmpleados):
    empleado=Empleados.objects.get(idEmpleados=idEmpleados)
    empleado.delete()
    return redirect("empleados")