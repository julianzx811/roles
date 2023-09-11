from django.db import models

# Create your models here.
class Estudiante(models.Model):
    programa = models.CharField(max_length=10)
    codigo = models.IntegerField()
    email_institucional = models.EmailField()
    email_personal = models.EmailField()
    telefono = models.IntegerField()
    nombre = models.CharField(max_length=50)
    periodo_lectivo = models.CharField(max_length=10, default='2023-1')
