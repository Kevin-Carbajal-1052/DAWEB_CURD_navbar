from django.shortcuts import render,redirect
from .models import Categoria
# Create your views here.
def inicio_vistaCategorias(request):
    lascategorias=Categoria.objects.all()
    return render(request, 'gestionarCategoria.html',{'miscategorias':lascategorias})

def registrarCategorias(request):
    idCategoria=request.POST["idCategoria"]
    Nombre=request.POST["Nombre"]
    idProducto=request.POST["idProducto"]
    Promociones=request.POST["Promociones"]
    Tamaño=request.POST["Tamaño"]
    Color=request.POST["Color"]
    Genero=request.POST["Genero"]
    guardarcategoria=Categoria.objects.create(idCategoria=idCategoria,Nombre=Nombre,idProducto=idProducto,Promociones=Promociones,Tamaño=Tamaño,Color=Color,Genero=Genero)
    return redirect('categorias')

def seleccionarCategorias(request,idCategoria):
    categoria=Categoria.objects.get(idCategoria=idCategoria)
    return render(request,"editarCategoria.html",{"miscategorias":categoria})

def editarCategoria(request):
    idCategoria=request.POST["idCategoria"]
    Nombre=request.POST["Nombre"]
    idProducto=request.POST["idProducto"]
    Promociones=request.POST["Promociones"]
    Tamaño=request.POST["Tamaño"]
    Color=request.POST["Color"]
    Genero=request.POST["Genero"]
    categoria=Categoria.objects.get(idCategoria=idCategoria)
    categoria.idCategoria=idCategoria
    categoria.Nombre=Nombre
    categoria.idProducto=idProducto
    categoria.Promociones=Promociones
    categoria.Tamaño=Tamaño
    categoria.Color=Color
    categoria.Genero=Genero
    categoria.save()
    return redirect('categorias')

def borrarCategoria(request,idCategoria):
    categoria=Categoria.objects.get(idCategoria=idCategoria)
    categoria.delete()
    return redirect('categorias')