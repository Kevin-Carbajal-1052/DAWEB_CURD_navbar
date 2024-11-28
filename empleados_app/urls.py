from django.urls import path
from empleados_app import views
urlpatterns = [
    path("empleados",views.inicio_vistaEmpleados,name="empleados"),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path("borrarEmpleado/<idEmpleados>",views.borrarEmpleado,name="borrarEmpleado"),
    path("seleccionarEmpleados/<idEmpleados>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleado/",views.editarEmpleado,name="editarEmpleado")
]