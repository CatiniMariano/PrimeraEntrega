# Generated by Django 4.1.3 on 2022-11-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerapp', '0002_alter_familia_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
