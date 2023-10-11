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
    periodo_lectivo = models.CharField(max_length=255, default="2024 1", null="2024 1")
    plan_estudios = models.OneToOneField(
        Plan_estudios, on_delete=models.CASCADE, null=True
    )
    def actualizar_periodo(self):
        # Verificar si el estado de ubicación indica que el estudiante no aprobó o aplazó
        if self.estadopractica_set.filter(estado_ubicación__in=["NO APROBADO", "APLAZA 2024 1", "Aplaza 2024 1"]):
            # Obtener el último periodo registrado en la base de datos
            ultimo_periodo = self.estadopractica_set.latest('id').periodo_practica
            # Dividir el periodo en año y número de periodo
            periodo_anio, periodo_numero = ultimo_periodo.split()
            # Convertir el número de periodo a entero
            periodo_numero = int(periodo_numero)
            # Calcular el nuevo periodo
            if periodo_numero == 1:
                # Si estaba en el primer periodo, avanzamos al segundo del mismo año
                nuevo_periodo = f"{periodo_anio} 2"
            elif periodo_numero == 2:
                # Si estaba en el segundo periodo, avanzamos al primero del siguiente año
                nuevo_anio = int(periodo_anio) + 1
                nuevo_periodo = f"{nuevo_anio} 1"
            else:
                # Si no es 1 ni 2, dejamos el periodo sin cambios
                nuevo_periodo = ultimo_periodo

            # Actualizar el campo periodo_lectivo del estudiante
            self.periodo_lectivo = nuevo_periodo
            self.save()


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
    codigo_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    practica_Donde_Labora_EmpresaFliar_Emprendim_Otro = models.CharField(
        max_length=255, null=True
    )
    estado_ubicación = models.CharField(max_length=255, null=True)
    comentarios = models.CharField(max_length=255, null=True)
    codigo_estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    item = models.OneToOneField(Aspirantes, on_delete=models.CASCADE)
    id_contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE)


class monitores(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    codigo = models.CharField(max_length=255, null=False)
    correo_institucional = models.CharField(
        primary_key=True, max_length=500, null=False
    )
    horas_disponibles = models.IntegerField()
    programa = models.CharField(default="sin programa", max_length=255, null=False)

class Perfiles(models.Model):
    contrasena =  models.CharField(max_length=255,null=False)
    codigo = models.CharField(max_length=255,null=False, default='1')
    nombre = models.CharField(max_length=255,null=False)
    cargo = models.CharField(max_length=255,null=False)
