from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.
def inicio_vistaProductos(request):
    losproductos=Productos.objects.all()
    return render(request, 'gestionarProductos.html',{'misproductos':losproductos})

def registrarProductos(request):
    idProductos=request.POST["idProductos"]
    Nombre=request.POST["Nombre"]
    Precio=request.POST["Precio"]
    idCategoria=request.POST["idCategoria"]
    idProvedores=request.POST["idProvedores"]
    Descripcion=request.POST["Descripcion"]
    CantidadStock=request.POST["CantidadStock"]
    guardarorden=Productos.objects.create(idProductos=idProductos,Nombre=Nombre,Precio=Precio,idCategoria=idCategoria,idProvedores=idProvedores,Descripcion=Descripcion,CantidadStock=CantidadStock)
    return redirect('productos')

def seleccionarProductos(request,idProductos):
    productos=Productos.objects.get(idProductos=idProductos)
    return render(request,"editarproductos.html",{"misproductos":productos})

def editarProductos(request):
    idProductos=request.POST["idProductos"]
    Nombre=request.POST["Nombre"]
    Precio=request.POST["Precio"]
    idCategoria=request.POST["idCategoria"]
    idProvedores=request.POST["idProvedores"]
    Descripcion=request.POST["Descripcion"]
    CantidadStock=request.POST["CantidadStock"]
    productos=Productos.objects.get(idProductos=idProductos)
    productos.Nombre=Nombre
    productos.Precio=Precio
    productos.idCategoria=idCategoria
    productos.idProvedores=idProvedores
    productos.Descripcion=Descripcion
    productos.CantidadStock=CantidadStock
    productos.save()
    return redirect('productos')

def borrarProductos(request,idProductos):
    productos=Productos.objects.get(idProductos=idProductos)
    productos.delete()
    return redirect("productos")