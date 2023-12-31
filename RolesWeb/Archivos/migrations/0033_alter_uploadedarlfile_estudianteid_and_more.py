# Generated by Django 4.2.5 on 2023-10-29 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0032_uploadedarlfile_uploadedepsfile_uploadedlaboralfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedarlfile',
            name='estudianteId',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Archivos.estudiante'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadedepsfile',
            name='estudianteId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Archivos.estudiante'),
        ),
        migrations.AlterField(
            model_name='uploadedlaboralfile',
            name='estudianteId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Archivos.estudiante'),
        ),
    ]
