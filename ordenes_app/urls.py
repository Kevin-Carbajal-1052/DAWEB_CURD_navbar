from django.urls import path
from ordenes_app import views
urlpatterns = [
    path("ordenes",views.inicio_vistaOrdenes,name="ordenes"),
    path("registrarOrdenes/",views.registrarOrdenes,name="registrarOrdenes"),
    path("borrarOrden/<idOrdenes>",views.borrarOrden,name="borrarOrden"),
    path("seleccionarOrdenes/<idOrdenes>",views.seleccionarOrdenes,name="seleccionarOrdenes"),
    path("editarOrden/",views.editarOrden,name="editarOrden")
]