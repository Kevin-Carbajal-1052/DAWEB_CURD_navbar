from django.urls import path
from categoria_app import views
urlpatterns = [
    path("categorias",views.inicio_vistaCategorias,name="categorias"),
    path("registrarCategorias/",views.registrarCategorias,name="registrarCategorias"),
    path("borrarCategoria/<idCategoria>",views.borrarCategoria,name="borrarCategoria"),
    path("seleccionarCategorias/<idCategoria>",views.seleccionarCategorias,name="seleccionarCategorias"),
    path("editarCategoria/",views.editarCategoria,name="editarCategoria")
]