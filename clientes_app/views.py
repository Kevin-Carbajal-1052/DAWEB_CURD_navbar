from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.
def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all()
    return render(request, 'gestionarClientes.html',{'misclientes':losclientes})

def registrarClientes(request):
    idClientes=request.POST["idClientes"]
    Nombre=request.POST["Nombre"]
    Telefono=request.POST["Telefono"]
    Direccion=request.POST["Direccion"]
    Correo=request.POST["Correo"]
    FechaRegistro=request.POST["FechaRegistro"]
    guardarcliente=Clientes.objects.create(idClientes=idClientes,Nombre=Nombre,Telefono=Telefono,Direccion=Direccion,Correo=Correo,FechaRegistro=FechaRegistro)
    return redirect('clientes')

def seleccionarClientes(request,idClientes):
    cliente=Clientes.objects.get(idClientes=idClientes)
    return render(request,"editarClientes.html",{"misclientes":cliente})

def editarCliente(request):
    idClientes=request.POST["idClientes"]
    Nombre=request.POST["Nombre"]
    Telefono=request.POST["Telefono"]
    Direccion=request.POST["Direccion"]
    Correo=request.POST["Correo"]
    FechaRegistro=request.POST["FechaRegistro"]
    cliente=Clientes.objects.get(idClientes=idClientes)
    cliente.idClientes=idClientes
    cliente.Nombre=Nombre
    cliente.Telefono=Telefono
    cliente.Direccion=Direccion
    cliente.Correo=Correo
    cliente.FechaRegistro=FechaRegistro
    cliente.save()
    return redirect('clientes')

def borrarCliente(request,idClientes):
    cliente=Clientes.objects.get(idClientes=idClientes)
    cliente.delete()
    return redirect("clientes")