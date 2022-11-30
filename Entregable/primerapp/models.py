from django.db import models
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)

# Create your models here.
class familia(models.Model):
    nombre= models.CharField(max_length=30)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField()




    
