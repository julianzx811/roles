# Generated by Django 4.1.10 on 2023-10-16 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0023_estudiante_docente_asignado_monitores_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='docente_asignado',
            field=models.OneToOneField(default='Ningun', null=True, on_delete=django.db.models.deletion.CASCADE, to='Archivos.monitores'),
        ),
    ]