from django.urls import path
# imprtando las vistas
from . import views

urlpatterns = [
    path("", views.index),
    path("login/", views.log_in),
    path("administrador/", views.admin),
    path("empleado/", views.empledo),
    path("tecnico/", views.tecnico),
    # empleado
    path("solicitud/", views.solicitud_view),
    path("registro-solicitud/", views.registro_solicitud)
    # administrador
    # tecnico
]