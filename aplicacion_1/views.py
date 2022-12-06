from django.shortcuts import render
from .models import familiar
from django.http import HttpResponse
# Create your views here.

def familiar(request):

    familiar_1= familiar(nombre= "jose", edad= 18, fecha_de_nac=20/12/2002)
    familiar_1.save()
    cadena_texto=f"familiar guardado{familiar_1.nombre},{familiar_1.edad}, {familiar_1.fecha_de_nac}"
    return HttpResponse(cadena_texto)
