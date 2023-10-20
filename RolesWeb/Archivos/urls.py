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
    path("vistaCoordinador/AsignacionDocentesEstudiantes/", views.AsignacionDocentesEstudiantes, name="AsignacionDocentesEstudiantes"),
    path("CrearMonitor/", views.CrearMonitor, name="CrearMonitor"),
    path("MostrarEstudiantes/", views.MostrarEstudiantes, name="MostrarEstudiantes"),
    # CRUD operations for programs
    path("vistaCoordinador/CrudProgramas/", views.CrudPrograma, name="CrudProgramas"),
    path("CreatePrograma/", views.CreatePrograma, name="CreatePrograma"),
    path(
        "UpdatePrograma/<int:programa_id>/", views.UpdatePrograma, name="UpdatePrograma"
    ),
    path(
        "DeletePrograma/<int:programa_id>/", views.DeletePrograma, name="DeletePrograma"
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
    path("upload/", views.upload_file, name="upload_file"),
    path("files/", views.list_files, name="list_files"),
    path("view_file/", views.view_file, name="view_file"),
    path(
        "vistaEstudiante/iniciarPractica/", views.iniciar_practicas, name="list_files"
    ),
    path(
        "vistaEstudiante/iniciarPractica/SubirContranoLaboral/",
        views.SubirContranoLaboral,
        name="list_files",
    ),
    path(
        "vistaEstudiante/iniciarPractica/SubirAfiliacionARL/",
        views.SubirAfiliacionARL,
        name="list_files",
    ),
    path(
        "vistaEstudiante/iniciarPractica/SubirDocumentoEPS/",
        views.SubirDocumentoEPS,
        name="list_files",
    ),
    path(
        "vistaEstudiante/iniciarPractica/DocumentosSubidos/",
        views.DocumentosSubidos,
        name="list_files",
    ),
    path("files/<int:file_id>/", views.view_file, name="view_file"),
]
