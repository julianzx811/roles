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
        "AsignacionDocentesEstudiantes/",
        views.AsignacionDocentesEstudiantes,
        name="AsignacionDocentesEstudiantes",
    ),
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
        "vistaLiderOficinaPracticas/",
        views.indexOficinaPracticas,
        name="vistaOficinaPracticas",
    ),
    path(
        "vistaAuxiliarOficinaPracticas/",
        views.indexAuxiliarOficinaPracticas,
        name="vistaAuxiliarOficinaPracticas",
    ),
    path(
        "vistaAdministrador/",
        views.indexAdministrador,
        name="vistaAdministrador",
    ),
    path(
        "agregarNuevoLider/",
        views.agregarNuevoLider,
        name="agregarNuevoLider",
    ),
    path(
        "CrudPrograma/",
        views.CrudPrograma,
        name="CrudPrograma",
    ),
    path(
        "agregarNuevoAuxiliar/",
        views.agregarNuevoAuxiliar,
        name="agregarNuevoAuxiliar",
    ),
    path(
        "administrarSemestres", views.administrarSemestres, name="administrarSemestres"
    ),
    path("CrearSemestre/", views.CreateSemestre, name="CrearSemestre"),
    path("UpdateSemestre/<int:id>/", views.UpdateSemestre, name="UpdateSemestre"),
    path("DeleteSemestre/<int:id>/", views.DeleteSemestre, name="DeleteSemestre"),
    path(
        "asignarNuevoCoordinador/",
        views.asignarNuevoCoordinador,
        name="asignarNuevoCoordinador",
    ),
    path(
        "vistaDocenteMonitor/",
        views.indexDocenteMonitor,
        name="vistaDocenteMonitor",
    ),
    path(
        "vistaEstudiante/<str:estudiante_id>/",
        views.indexEstudiante,
        name="vistaEstudiante",
    ),
    path("upload/", views.upload_file, name="upload_file"),
    path("files/<int:estudiante_id>/", views.list_files, name="list_files"),
    path("view_file/", views.view_file, name="view_file"),
    path(
        "vistaEstudiante/<str:estudiante_id>/iniciarPractica/",
        views.iniciar_practicas,
        name="iniciarpractiquica",
    ),
    path(
        "vistaEstudiante/<str:estudiante_id>/iniciarPractica/SubirContranoLaboral/",
        views.SubirContranoLaboral,
        name="subir_contrano_laboral",
    ),
    path(
        "vistaEstudiante/<str:estudiante_id>/iniciarPractica/SubirAfiliacionARL/",
        views.SubirAfiliacionARL,
        name="subir_afiliacion_arl",
    ),
    path(
        "vistaEstudiante/<str:estudiante_id>/iniciarPractica/SubirDocumentoEPS/",
        views.SubirDocumentoEPS,
        name="subir_documento_eps",
    ),
    path(
        "vistaEstudiante/<str:estudiante_id>/iniciarPractica/DocumentosSubidos/",
        views.DocumentosSubidos,
        name="documentos_subidos",
    ),
    path("files/<int:file_id>/", views.view_file, name="view_file"),
]
