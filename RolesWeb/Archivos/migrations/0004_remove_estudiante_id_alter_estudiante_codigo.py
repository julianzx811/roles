# Generated by Django 4.2.5 on 2023-09-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0003_estudiante_periodo_lectivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
