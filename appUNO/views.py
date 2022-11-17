from django.http import HttpResponse
from appUNO.models import Curso
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "appUNO/index.html")


def cursos(request):
    return render(request, "appUNO/cursos.html")


def estudiantes(request):
    return render(request, "appUNO/estudiantes.html")


def profesores(request):
    return render(request, "appUNO/profesores.html")


def entregables(request):
    return render(request, "appUNO/entregables.html")



def listado_cursos(request):
    cursos = Curso.objects.all()

    cadena_respuesta = ""
    for curso in cursos:
        cadena_respuesta += f"({curso.nombre}, {curso.camada})" + " | "

    return HttpResponse(cadena_respuesta)