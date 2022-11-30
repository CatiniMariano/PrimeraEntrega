from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def familiar(request):
    primer_familiar = familia(nobmre="Silvia Mattei",edad = 58, nacionalidad = "Argentina", fecha_de_nacimiento = (19,12,1964))
    segundo_familiar = familia(nobmre="Marcelo Catini",edad = 58, nacionalidad = "Argentina", fecha_de_nacimiento = (10,11,1964))
    tercer_familiar = familia(nobmre="Mateo Catini",edad = 23, nacionalidad = "Argentina", fecha_de_nacimiento = (21,12,1999) )
    primer_familiar.save()
    segundo_familiar.save()
    tercer_familiar.save()
    return render ('./Templates/templates.html')








