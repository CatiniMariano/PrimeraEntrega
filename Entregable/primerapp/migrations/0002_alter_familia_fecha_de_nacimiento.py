# Generated by Django 4.1.3 on 2022-11-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
    ]
