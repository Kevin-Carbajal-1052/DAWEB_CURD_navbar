from django.urls import path
from proveedor_app import views
urlpatterns = [
    path("proveedor",views.inicio_vistaProveedor,name="proveedor"),
    path("registrarProveedores/",views.registrarProveedores,name="registrarProveedores"),
    path("borrarProveedor/<idProveedor>",views.borrarProveedor,name="borrarProveedor"),
    path("seleccionarProveedores/<idProveedor>",views.seleccionarProveedores,name="seleccionarProveedores"),
    path("editarProveedor/",views.editarProveedor,name="editarProveedor")
]