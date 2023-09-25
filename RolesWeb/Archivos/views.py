import openpyxl
import psycopg2
from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiante, Aspirantes, Contrato, Estado_Practica


def index(request):
    return render(request, "Archivos/index.html")


def cargarArchivoEstudiantes(request):
    if request.method == "GET":
        return render(request, "Archivos/cargaEstudiantes.html", {})
    else:
        try:
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
                if len(row_data) >= 7:  # Verificar si hay suficientes elementos en la lista
                    excel_data.append(row_data)
                else:
                    print(f"La fila no tiene suficientes elementos: {row_data}")

            for datos in excel_data:
                est1 = Estudiante(
                    codigo=datos[2],
                    programa=datos[1],
                    email_institucional=datos[3],
                    email_personal=datos[4],
                    telefono=datos[5],
                    nombre=datos[6],
                    periodo_lectivo=periodo,
                )
                est1.save()

            return render(
                request, "Archivos/cargaEstudiantes.html", {"excel_data": excel_data}
            )
        except Exception as error:
            print(error)
            return render(
                request, "Archivos/cargaEstudiantes.html", {"error": str(error)}
            )

def cargarArchivoEstudiantesDos(request):
    if request.method == "GET":
        return render(request, "Archivos/cargaEstudiantesDos.html", {})
    else:
        try:
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["ING SISTEMAS 2023 2"] # Utiliza la hoja activa o ajusta según la hoja que necesites

            excel_data = []

            for row in worksheet.iter_rows(values_only=True):
                row_data = list(row)
                excel_data.append(row_data)

            for row in excel_data:
                # Verifica si la fila tiene suficientes elementos para procesar
                if len(row) >= 28:  # Ajusta el número según la cantidad de columnas en tu Excel
                    # Crear un objeto Estudiante
                    estudiante = Estudiante(
                        codigo=row[0],
                        programa=row[1],
                        email_institucional=row[2],
                        email_personal=row[3],
                        telefono=row[4],
                        nombre=row[5],
                        apellidos=row[6],
                        cedula=row[7],
                        celular=row[8],
                        periodo_lectivo=row[9],
                        # Ajusta esto para el campo plan_estudios
                    )
                    estudiante.save()

                    # Crear un objeto Aspirantes relacionado con el estudiante
                    aspirantes = Aspirantes(
                        periodo_practica=row[10],
                        aprobación_Programa=row[11],
                        matriculado_Academica_y_Financieramente=row[12],
                        inscripcion=row[13],
                        curso_induccion_y_rl=row[14],
                        ruta_preparacion_vida_laboral=row[15],
                        envio_hv=row[16],
                        titulo_tecnico_o_tecnologo=row[17],
                        codigo_estudiante=estudiante,
                    )
                    aspirantes.save()

                    # Crear un objeto Contrato relacionado con el estudiante
                    contrato = Contrato(
                        tipo_Contrato=row[18],
                        fecha_Inicio=row[19],
                        fecha_Final=row[20],
                        encargado_Proceso_Seleccion=row[21],
                        datos_Tutor_O_Jefe_Directivo=row[22],
                        documentos_Pendientes=row[23],
                        sector=row[24],
                    )
                    contrato.save()

                    # Crear un objeto Estado_Practica relacionado con el estudiante, Aspirantes y Contrato
                    estado_practica = Estado_Practica(
                        codigo_estudiante=estudiante,
                        practica_Donde_Labora_EmpresaFliar_Emprendim_Otro=row[25],
                        estado_ubicación=row[26],
                        comentarios=row[27],
                        item=aspirantes,
                        id_contrato=contrato,
                    )
                    estado_practica.save()

            return render(
                request, "Archivos/cargaEstudiantesDos.html", {"excel_data": excel_data}
            )
        except Exception as error:
            print(error)
            return render(
                request, "Archivos/cargaEstudiantesDos.html", {"error": str(error)}
            )