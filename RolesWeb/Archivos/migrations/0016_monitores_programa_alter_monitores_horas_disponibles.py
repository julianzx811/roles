# Generated by Django 4.2.5 on 2023-10-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0015_monitores'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitores',
            name='programa',
            field=models.CharField(default='sin programa', max_length=255),
        ),
        migrations.AlterField(
            model_name='monitores',
            name='horas_disponibles',
            field=models.IntegerField(),
        ),
    ]
