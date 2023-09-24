from django.db import models


class Plan_estudios(models.Model):
    jornada = models.CharField(max_length=255, null=True)


class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True, max_length=255, null=False)
    programa = models.CharField(max_length=255, null=False)
    email_institucional = models.EmailField(null=False)
    email_personal = models.EmailField(null=False)
    telefono = models.CharField(max_length=255, null=False)
    nombre = models.CharField(max_length=255, null=False)
    apellidos = models.CharField(max_length=255, null=True)
    cedula = models.CharField(max_length=255, null=True)
    celular = models.CharField(max_length=255, null=True)
    periodo_lectivo = models.CharField(max_length=255, default="2024-1", null=False)
    plan_estudios = models.OneToOneField(
        Plan_estudios, on_delete=models.CASCADE, null=True
    )


class Aspirantes(models.Model):
    periodo_practica = models.CharField(max_length=255, null=False)
    aprobación_Programa = models.CharField(max_length=255, null=False)
    matriculado_Academica_y_Financieramente = models.CharField(
        max_length=255, null=False
    )
    inscripcion = models.CharField(max_length=255, null=False)
    curso_induccion_y_rl = models.CharField(max_length=255, null=False)
    ruta_preparacion_vida_laboral = models.CharField(max_length=255, null=False)
    envio_hv = models.CharField(max_length=255, null=False)
    titulo_tecnico_o_tecnologo = models.CharField(max_length=255, null=False)
    codigo_estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)


class Contrato(models.Model):
    tipo_Contrato = models.CharField(max_length=255, null=False)
    fecha_Inicio = models.CharField(max_length=255, null=False)
    fecha_Final = models.CharField(max_length=255, null=False)
    encargado_Proceso_Seleccion = models.CharField(max_length=255, null=False)
    datos_Tutor_O_Jefe_Directivo = models.CharField(max_length=255, null=False)
    documentos_Pendientes = models.CharField(max_length=255, null=False)
    sector = models.CharField(max_length=255, null=False)


class Estado_Practica(models.Model):
    codigo_estudiante = models.CharField(max_length=255, null=True)
    practica_Donde_Labora_EmpresaFliar_Emprendim_Otro = models.CharField(
        max_length=255, null=True
    )
    estado_ubicación = models.CharField(max_length=255, null=True)
    comentarios = models.CharField(max_length=255, null=True)
    codigo_estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    item = models.OneToOneField(Aspirantes, on_delete=models.CASCADE)
    id_contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE)
