# Generated by Django 4.1.10 on 2023-10-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0016_monitores_programa_alter_monitores_horas_disponibles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
            ],
        ),
    ]
