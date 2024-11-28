from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.
def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request, 'gestionarProveedores.html',{'misproveedores':losproveedores})

def registrarProveedores(request):
    idProveedor=request.POST["idProveedor"]
    Nombre=request.POST["Nombre"]
    Telefono=request.POST["Telefono"]
    Correo=request.POST["Correo"]
    Direccion=request.POST["Direccion"]
    TipoProducto=request.POST["TipoProducto"]
    guardarproveedor=Proveedor.objects.create(idProveedor=idProveedor,Nombre=Nombre,Telefono=Telefono,Correo=Correo,Direccion=Direccion,TipoProducto=TipoProducto)
    return redirect('proveedor')

def seleccionarProveedores(request,idProveedor):
    proveedor=Proveedor.objects.get(idProveedor=idProveedor)
    return render(request,"editarProveedores.html",{"misproveedores":proveedor})

def editarProveedor(request):
    idProveedor=request.POST["idProveedor"]
    Nombre=request.POST["Nombre"]
    Telefono=request.POST["Telefono"]
    Correo=request.POST["Correo"]
    Direccion=request.POST["Direccion"]
    TipoProducto=request.POST["TipoProducto"]
    proveedor=Proveedor.objects.get(idProveedor=idProveedor)
    proveedor.idProveedor=idProveedor
    proveedor.Nombre=Nombre
    proveedor.Telefono=Telefono
    proveedor.Correo=Correo
    proveedor.Direccion=Direccion
    proveedor.TipoProducto=TipoProducto
    proveedor.save()
    return redirect('proveedor')

def borrarProveedor(request,idProveedor):
    proveedor=Proveedor.objects.get(idProveedor=idProveedor)
    proveedor.delete()
    return redirect("proveedor")