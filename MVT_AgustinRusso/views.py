from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def vista_saludo(request):

    return HttpResponse(""" 
    <h1> Hola coders! :) </h1> 
    <p style="color:red"> Esto es una prueba <p>
    """)



def iniciar_sesion(request):

    return HttpResponse(" Pasame tu username y tu password por WhatsApp ;) ")



def dia_hoy(request, nombre):

    hoy = datetime.now()
    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"

    return HttpResponse(respuesta)



def vista_edad(request, edad):

    edad = int(edad) 
    resultado = datetime.now().year - edad

    return HttpResponse(f"Naciste en el año {resultado}")



def vista_plantilla(request):

    archivo = open(r"/Users/agustin/Documents/MVTAgustinRusso/codigo/MVT_AgustinRusso/templates/plantilla_bonita.html")
    #archivo = open("./templates/plantilla_bonita.html")
    plantilla = Template(archivo.read())
    archivo.close()

    datos = {"nombre": "Agustin", "fecha": datetime.now(), "apellido": "Russo", "edad": 32}

    contexto = Context(datos)
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

