from django.urls import path
from clientes_app import views
urlpatterns = [
    path("clientes",views.inicio_vistaClientes,name="clientes"),
    path("registrarClientes/",views.registrarClientes,name="registrarClientes"),
    path("borrarCliente/<idClientes>",views.borrarCliente,name="borrarCliente"),
    path("seleccionarClientes/<idClientes>",views.seleccionarClientes,name="seleccionarClientes"),
    path("editarCliente/",views.editarCliente,name="editarCliente")
]