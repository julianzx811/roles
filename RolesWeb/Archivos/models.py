from django.db import models

# Create your models here.
class Estudiante(models.Model):
    programa = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    email_institucional = models.EmailField()
    email_personal = models.EmailField()
    telefono = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    periodo_lectivo = models.CharField(max_length=255, default='2024-1')
