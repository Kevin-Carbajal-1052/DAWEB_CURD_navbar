from django.shortcuts import render,redirect
from .models import Ordenes
# Create your views here.
def inicio_vistaOrdenes(request):
    lasordenes=Ordenes.objects.all()
    return render(request, 'gestionarOrdenes.html',{'misordenes':lasordenes})

def registrarOrdenes(request):
    idOrdenes=request.POST["txtidOrdenes"]
    idClientes=request.POST["txtidClientes"]
    FechaOrden=request.POST["FechaOrden"]
    Cantidad=request.POST["Cantidad"]
    FechaEnvio=request.POST["FechaEnvio"]
    DireccionEnvio=request.POST["DireccionEnvio"]
    idEmpleado=request.POST["idEmpleado"]
    idProducto=request.POST["idProducto"]
    guardarorden=Ordenes.objects.create(idOrdenes=idOrdenes,idClientes=idClientes,FechaOrden=FechaOrden,Cantidad=Cantidad,FechaEnvio=FechaEnvio,DireccionEnvio=DireccionEnvio,idEmpleado=idEmpleado,idProducto=idProducto)
    return redirect('ordenes')

def seleccionarOrdenes(request,idOrdenes):
    orden=Ordenes.objects.get(idOrdenes=idOrdenes)
    return render(request,"editarorden.html",{"misordenes":orden})

def editarOrden(request):
    idOrdenes=request.POST["txtidOrdenes"]
    idClientes=request.POST["txtidClientes"]
    FechaOrden=request.POST["FechaOrden"]
    Cantidad=request.POST["Cantidad"]
    FechaEnvio=request.POST["FechaEnvio"]
    DireccionEnvio=request.POST["DireccionEnvio"]
    idEmpleado=request.POST["idEmpleado"]
    idProducto=request.POST["idProducto"]
    orden=Ordenes.objects.get(idOrdenes=idOrdenes)
    orden.idOrdenes=idOrdenes
    orden.idClientes=idClientes
    orden.FechaOrden=FechaOrden
    orden.Cantidad=Cantidad
    orden.FechaEnvio=FechaEnvio
    orden.DireccionEnvio=DireccionEnvio
    orden.idEmpleado=idEmpleado
    orden.idProducto=idProducto
    orden.save()
    return redirect('ordenes')

def borrarOrden(request,idOrdenes):
    orden=Ordenes.objects.get(idOrdenes=idOrdenes)
    orden.delete()
    return redirect("ordenes")