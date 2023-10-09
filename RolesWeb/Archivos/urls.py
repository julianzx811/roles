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
    path("CrearMonitor/", views.CrearMonitor, name="CrearMonitor"),
    path("MostrarEstudiantes/", views.MostrarEstudiantes, name="MostrarEstudiantes"),
    # CRUD operations for programs
    path("CrudProgramas/", views.CrudPrograma, name="CrudProgramas"),
    path("CreatePrograma/", views.CreatePrograma, name="CreatePrograma"),
    path(
        "UpdatePrograma/<int:programa_id>/", views.UpdatePrograma, name="UpdatePrograma"
    ),
    path(
        "DeletePrograma/<int:programa_id>/", views.DeletePrograma, name="DeletePrograma"
    ),
]
