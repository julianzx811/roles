import openpyxl
import psycopg2
from django.http import HttpResponse
from django.shortcuts import render
from .models import Estudiante, Aspirantes, Contrato, Estado_Practica, Plan_estudios


archivo_subido = True

def index(request):
    existe = Estudiante.objects.exists()
    return render(request, "Archivos/index.html", {"archivo_subido":archivo_subido, "existe":existe})


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

                if (Estudiante.objects.filter(codigo=datos[2])):
                        est1 = Estudiante.objects.filter(codigo=datos[2])[0]
                        Estudiante.objects.filter(codigo=datos[2]).update(email_institucional=datos[3], email_personal=datos[4])
                else:
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
                
            archivo_subido = True
            return render(
                request, "Archivos/cargaEstudiantes.html", {"excel_data": excel_data, "archivo_subido": archivo_subido}
            )
            
        except Exception as error:
            print(error)
            return render(
                request, "Archivos/cargaEstudiantes.html", {"error": str(error)}
            )

def cargarArchivoEstudiantesDos(request):
    if request.method == "GET":
        # Realiza una consulta en la base de datos para verificar si existen datos en las columnas especificadas
        if Estudiante.objects.filter(
            programa__isnull=False,
            email_institucional__isnull=False,
            email_personal__isnull=False,
            telefono__isnull=False,
            nombre__isnull=False,
            periodo_lectivo__isnull=False,
        ).exists():
            # Si existen datos, permite la carga
            return render(request, "Archivos/cargaEstudiantesDos.html", {})
        else:
            # Si no existen datos, muestra un mensaje de error
            return render(request, "Archivos/cargaEstudiantesDos.html", {"error": "Por favor, primero carga datos en cargarArchivoEstudiantes."})
    else:
        try:
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            worksheet = wb["ING SISTEMAS 2023 2"] 

            excel_data = []

            for row in worksheet.iter_rows(min_row=4, max_col=28):
                row_data = []
                for cell in row:
                    if str(cell.value) != "None":
                        row_data.append(str(cell.value))
                if len(row_data) >= 7:  
                    excel_data.append(row_data)

            for row in excel_data:

                if len(row) >= 28:

                    
                    plan_estudios = Plan_estudios(
                        jornada=row[12]
                    )
                    plan_estudios.save()
                    
                    
                    if (Estudiante.objects.filter(codigo=row[7])):
                        estudiante = Estudiante.objects.filter(codigo=row[7])[0]
                        Estudiante.objects.filter(codigo=row[7]).update(nombre=row[5], apellidos=row[6], cedula=row[8], celular=row[9])
                    else:
                    
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
                            # Ajusta esto para el campo plan_estudios
                        )
                        estudiante.save()


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

                    
                    if(len(row)>23):

                        print('entro If')
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
                    else:
                        contrato = Contrato(
                            tipo_Contrato='null',
                            fecha_Inicio='null',
                            fecha_Final='null',
                            encargado_Proceso_Seleccion='null',
                            datos_Tutor_O_Jefe_Directivo='null',
                            documentos_Pendientes='null',
                            sector='null',
                        )
                        contrato.save()

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
                request, "Archivos/cargaEstudiantesDos.html", {"excel_data": excel_data}
            )
        except Exception as error:
            print(error)
            return render(
                request, "Archivos/cargaEstudiantesDos.html", {"error": str(error)}
            )



