# Generated by Django 4.2.7 on 2023-11-08 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0037_alter_semestres_fecha_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='periodo_lectivo',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
