# Generated by Django 4.2.5 on 2023-09-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0013_remove_estudiante_id_alter_estudiante_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='periodo_lectivo',
            field=models.CharField(default='2024-1', max_length=255, null='2024-1'),
        ),
    ]
