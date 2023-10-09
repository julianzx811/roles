from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
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
    path(
        "vistaCoordinador/",
        views.indexCoordinador,
        name="vistaCoordinador",
    ),
    path(
        "vistaDocenteMonitor/",
        views.indexDocenteMonitor,
        name="vistaDocenteMonitor",
    ),
    path(
        "vistaEstudiante/",
        views.indexEstudiante,
        name="vistaEstudiante",
    ),
]
