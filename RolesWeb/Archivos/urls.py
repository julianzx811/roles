from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cargaEstudiantes/", views.cargarArchivoEstudiantes, name="cargaEstudiantes"),
    path(
        "cargaEstudiantesDos/",
        views.cargarArchivoEstudiantesDos,
        name="cargaEstudiantesDos",
    ),
    path(
        "CrearMonitor/",
        views.CrearMonitor,
        name="CrearMonitor",
    ),
    path(
        "MostrarEstudiantes/",
        views.MostrarEstudiantes,
        name="MostrarEstudiantes",
    ),
]
