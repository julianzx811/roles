# Generated by Django 4.1.10 on 2023-10-16 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Archivos', '0025_alter_monitores_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitores',
            name='estado',
            field=models.BooleanField(default=1),
        ),
    ]