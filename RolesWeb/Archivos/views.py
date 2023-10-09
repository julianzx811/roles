import openpyxl
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import DatosForm, ProgramForm
from .models import (Aspirantes, Contrato, Estado_Practica, Estudiante,
                     Perfiles, Plan_estudios, Programa, monitores)

archivo_subido = True


def login(request):
    if request.method == "GET":
        return render(request, "Archivos/login.html")
    if request.method == "POST":
        login_fallo = False
        usuario_existe = False
        codigo = request.POST["codigo"]
        contrasena = request.POST["contrasena"]
        cargo = request.POST.get("cargoUsuario")
        print(codigo, contrasena, cargo)
        if Perfiles.objects.filter(codigo=codigo).exists():
            if (
                (Perfiles.objects.get(codigo=codigo).codigo == codigo)
                and (Perfiles.objects.get(codigo=codigo).contrasena == contrasena)
                and (Perfiles.objects.get(codigo=codigo).cargo == cargo)
            ):
                print("Login exitoso")
                if cargo == "Estudiante":
                    return redirect("/vistaEstudiante")
                elif cargo == "Docente Monitor":
                    return redirect(
                        "/vistaDocenteMonitor",
                    )
                elif cargo == "Coordinador":
                    return redirect("/vistaCoordinador")
            else:
                login_fallo = True
                return render(
                    request,
                    "Archivos/login.html",
                    {"login_fallo": login_fallo, "usuario_existe": usuario_existe},
                )
        else:
            usuario_existe = True
            return render(
                request,
                "Archivos/login.html",
                {"login_fallo": login_fallo, "usuario_existe": usuario_existe},
            )


def CrearMonitor(request):
    if request.method == "GET":
        return render(
            request, "Archivos/CrearMonitor.html", {"archivo_subido": archivo_subido}
        )
    else:
        creaMonitor = False
        monitorExiste = False
        form = DatosForm(request.POST)
        if form.is_valid():
            if (
                Perfiles.objects.filter(codigo=form.cleaned_data["codigo"]).exists()
                == False
            ):
                Nombre = form.cleaned_data["nombre"]
                Codigo = form.cleaned_data["codigo"]
                Correo = form.cleaned_data["correo"]
                Horas = form.cleaned_data["horas"]
                Programa = form.cleaned_data["programa"]
                monitor = monitores(
                    nombre=Nombre,
                    codigo=Codigo,
                    correo_institucional=Correo,
                    horas_disponibles=Horas,
                    programa=Programa,
                )
                monitor.save()
                perfil = Perfiles(
                    codigo=Codigo,
                    contrasena=Codigo,
                    nombre=Nombre,
                    cargo="Docente Monitor",
                )
                perfil.save()
                creaMonitor = True
            else:
                monitorExiste = True
        return render(
            request,
            "Archivos/CrearMonitor.html",
            {
                "archivo_subido": archivo_subido,
                "creaMonitor": creaMonitor,
                "monitorExiste": monitorExiste,
            },
        )


def crearPrograma(request):
    return render(request, "Archivos/CrudPrograma.html")


def index(request):
    if request.method == "GET":
        return render(request, "Archivos/index.html")


def indexCoordinador(request):
    existe = Estudiante.objects.exists()
    return render(
        request,
        "Archivos/vistaCoordinador.html",
        {"archivo_subido": archivo_subido, "existe": existe},
    )


def indexDocenteMonitor(request):
    existe = Estudiante.objects.exists()
    return render(
        request,
        "Archivos/index.html",
        "Archivos/vistaDocenteMonitor.html",
        {"archivo_subido": archivo_subido, "existe": existe},
    )


def indexEstudiante(request):
    existe = Estudiante.objects.exists()
    return render(
        request,
        "Archivos/vistaEstudiante.html",
        {"archivo_subido": archivo_subido, "existe": existe},
    )


def cargarArchivoEstudiantes(request):
    if request.method == "GET":
        return render(request, "Archivos/cargaEstudiantes.html", {})
    else:
        try:
            actualizados = 0
            agregados = 0
            excel_file = request.FILES["excel_file"]
            periodo = request.POST.get("file_type")

            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["Sheet1"]

            excel_data = []

            for row in worksheet.iter_rows(min_row=14, max_col=8):
                row_data = []
                for cell in row:
                    if str(cell.value) != "None":
                        row_data.append(str(cell.value))
                if (
                    len(row_data) >= 7
                ):  # Verificar si hay suficientes elementos en la lista
                    excel_data.append(row_data)
                else:
                    print(f"La fila no tiene suficientes elementos: {row_data}")

            for datos in excel_data:
                if Estudiante.objects.filter(codigo=datos[2]):
                    if (
                        (
                            (Estudiante.objects.get(codigo=datos[2]).nombre == datos[6])
                            == False
                        )
                        or (
                            (
                                Estudiante.objects.get(
                                    codigo=datos[2]
                                ).email_institucional
                                == datos[3]
                            )
                            == False
                        )
                        or (
                            (
                                Estudiante.objects.get(codigo=datos[2]).email_personal
                                == datos[4]
                            )
                            == False
                        )
                        or (
                            (
                                Estudiante.objects.get(codigo=datos[2]).telefono
                                == datos[5]
                            )
                            == False
                        )
                    ):
                        actualizados += 1
                        print(actualizados)
                        Estudiante.objects.filter(codigo=datos[2]).update(
                            email_institucional=datos[3],
                            email_personal=datos[4],
                            telefono=datos[5],
                            nombre=datos[6],
                        )
                else:
                    est1 = Estudiante(
                        codigo=datos[2],
                        programa=datos[1],
                        email_institucional=datos[3],
                        email_personal=datos[4],
                        telefono=datos[5],
                        nombre=datos[6],
                        periodo_lectivo="2023-2",
                    )
                    agregados += 1
                    print("agregados", agregados)
                    est1.save()
                    perfil = Perfiles(
                        codigo=datos[2],
                        contrasena=datos[2],
                        nombre=datos[6],
                        cargo="Estudiante",
                    )
                    perfil.save()
            return render(
                request,
                "Archivos/cargaEstudiantes.html",
                {
                    "excel_data": excel_data,
                    "agregados": agregados,
                    "actualizados": actualizados,
                },
            )

        except Exception as error:
            print(error)
            return render(
                request, "Archivos/CargaEstudiantes.html", {"error": str(error)}
            )


def cargarArchivoEstudiantesDos(request):
    existe = Estudiante.objects.exists()
    if request.method == "GET":
        return render(request, "Archivos/CargaEstudiantesDos.html", {})
    else:
        try:
            actualizados = 0
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["ING SISTEMAS 2023 2"]

            excel_data = []

            for row in worksheet.iter_rows(min_row=4, max_col=28):
                row_data = []
                for cell in row:
                    if str(cell.value) != "None":
                        row_data.append(str(cell.value))
                if (
                    len(row_data) >= 7
                ):  # Verificar si hay suficientes elementos en la lista
                    excel_data.append(row_data)

            for row in excel_data:
                # Verifica si la fila tiene suficientes elementos para procesar
                if (
                    len(row) >= 28
                ):  # Ajusta el número según la cantidad de columnas en tu Excel
                    # Crear un objeto Estudiante

                    plan_estudios = Plan_estudios(jornada=row[12])
                    plan_estudios.save()

                    if Estudiante.objects.filter(codigo=row[7]):
                        estudiante = Estudiante.objects.filter(codigo=row[7])[0]
                        Estudiante.objects.filter(codigo=row[7]).update(
                            nombre=row[5],
                            apellidos=row[6],
                            cedula=row[8],
                            celular=row[9],
                        )

                        estudiante = Estudiante(
                            programa=row[11],
                            codigo=row[7],
                            email_institucional=row[10],
                            email_personal=row[10],
                            telefono=row[9],
                            nombre=row[5],
                            apellidos=row[6],
                            cedula=row[8],
                            celular=row[9],
                            periodo_lectivo=row[1]
                            # Ajusta esto para el campo plan_estudios
                        )
                        actualizados += 1
                        estudiante.save()

                        # Crear un objeto Aspirantes relacionado con el estudiante
                        aspirantes = Aspirantes(
                            periodo_practica=row[1],
                            aprobación_Programa=row[2],
                            matriculado_Academica_y_Financieramente=row[4],
                            inscripcion=row[13],
                            curso_induccion_y_rl=row[14],
                            ruta_preparacion_vida_laboral=row[15],
                            envio_hv=row[16],
                            titulo_tecnico_o_tecnologo=row[17],
                            codigo_estudiante=estudiante,
                        )
                        aspirantes.save()

                        if "Aplaza" in row[1]:
                            periodo_aplazado = row[1].split("Aplaza ")[1]
                            estudiante.periodo_lectivo = periodo_aplazado
                            print(
                                "Peridodo despues de aplaza: "
                                + row[1].split("Aplaza")[1]
                            )
                        elif row[1] == "NO APROBADO":
                            estudiante.periodo_lectivo = "suspendido"

                        estudiante.save()

                        # Crear un objeto Contrato relacionado con el estudiante
                        print("entro If")
                        contrato = Contrato(
                            tipo_Contrato=row[21],
                            fecha_Inicio=row[22],
                            fecha_Final=row[23],
                            encargado_Proceso_Seleccion=row[24],
                            datos_Tutor_O_Jefe_Directivo=row[25],
                            documentos_Pendientes=row[26],
                            sector=row[27],
                        )
                        contrato.save()

                        # Crear un objeto Estado_Practica relacionado con el estudiante, Aspirantes y Contrato
                        estado_practica = Estado_Practica(
                            codigo_estudiante=estudiante,
                            practica_Donde_Labora_EmpresaFliar_Emprendim_Otro=row[18],
                            estado_ubicación=row[19],
                            comentarios=row[20],
                            item=aspirantes,
                            id_contrato=contrato,
                        )
                        estado_practica.save()

            return render(
                request,
                "Archivos/CargaEstudiantesDos.html",
                {
                    "excel_data": excel_data,
                    "existe": existe,
                    "actualizados": actualizados,
                },
            )
        except Exception as error:
            print(error)
            return render(
                request, "Archivos/CargaEstudiantesDos.html", {"error": str(error)}
            )


def MostrarEstudiantes(request):
    estudiantes = Estudiante.objects.filter()
    return render(request, "Archivos/verEstudiantes.html", {"estudiantes": estudiantes})


def CrudPrograma(request):
    programas = Programa.objects.all()
    if request.method == "DELETE":
        return render(request, "Archivos/CrudPrograma.html", {"programas": programas})
    if request.method == "GET":
        return render(request, "Archivos/CrudPrograma.html", {"programas": programas})
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            try:
                codigo = form.cleaned_data["codigo"]
                programa = form.cleaned_data["programa"]
                facultad = request.POST.get("facultad")
                programita = Programa(
                    codigo=codigo, programa=programa, facultad=facultad
                )
                programita.save()
                return render(
                    request,
                    "Archivos/CrudPrograma.html",
                    {
                        "programas": programas,
                        "hecho": "se registro el monitor correctamente",
                    },
                )
            except Exception as error:
                print(error)
                return render(
                    request,
                    "Archivos/CrudPrograma.html",
                    {"error": error, "programas": programas},
                )
        else:
            print(form.errors)
            return render(
                request,
                "Archivos/CrearMonitor.html",
                {"error": form.errors, "programas": programas},
            )


def UpdatePrograma(request, programa_id):
    if request.method == "GET":
        programa = Programa.objects.get(pk=programa_id)
        programaobj = model_to_dict(programa)
        return render(
            request, "Archivos/UpdatePrograma.html", {"programa": programaobj}
        )
    elif request.method == "POST":
        print("entro1")
        form = ProgramForm(request.POST)
        if form.is_valid():
            try:
                print("entro2")
                codigo = form.cleaned_data["codigo"]
                programa = form.cleaned_data["programa"]
                facultad = request.POST.get("facultad")
                programita = Programa(
                    codigo=codigo, programa=programa, facultad=facultad
                )
                print(programita)
                programita.save()
            except Exception as error:
                print(error)
                return UpdatePrograma(request, programa_id)


def CreatePrograma(request):
    return render(request, "Archivos/CreatePrograma.html")


def DeletePrograma(request, programa_id):
    programa = Programa.objects.get(pk=programa_id)
    try:
        programa.delete()
        return CrudPrograma(request)
    except Exception as error:
        print(error)
        return CrudPrograma(request)
