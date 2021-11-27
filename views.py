from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso

# Create your views here.

def ver_curso(request):
    curso = Curso(nombre="prueba", camada = 4)
    curso.save

    return HttpResponse(f'{curso.nombre} {curso.camada}')