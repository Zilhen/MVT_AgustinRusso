from django.http import HttpResponse
from appUNO.models import Curso
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "appUNO/index.html")



def cursos(request):
    return HttpResponse("Estas en el Cursos")


def estudiantes(request):
    return HttpResponse("Estas en el Estudiantes")


def profesores(request):
    return HttpResponse("Estas en el Profesores")


def entregables(request):
    return HttpResponse("Estas en el Entregables")



def listado_cursos(request):
    cursos = Curso.objects.all()

    cadena_respuesta = ""
    for curso in cursos:
        cadena_respuesta += f"({curso.nombre}, {curso.camada})" + " | "

    return HttpResponse(cadena_respuesta)