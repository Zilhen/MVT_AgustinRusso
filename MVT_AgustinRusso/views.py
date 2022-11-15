from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader


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

    archivo = open("/Users/agustin/Documents/MVTAgustinRusso/codigo/MVT_AgustinRusso/templates/plantilla_bonita.html")
    #archivo = open("./templates/plantilla_bonita.html")
    plantilla = Template(archivo.read())
    archivo.close()

    datos = {"nombre": "Agustin", "fecha": datetime.now(), "apellido": "Russo", "edad": 32}

    contexto = Context(datos)
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos(request):

    #abrimos el archivo
    archivo = open("/Users/agustin/Documents/MVTAgustinRusso/codigo/MVT_AgustinRusso/templates/listado_alumnos.html")

    #creamos el template
    plantilla = Template(archivo.read())

    #cerramos archivo
    archivo.close()

    #creamos diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    #creamos el contexto
    contexto = Context(datos)
    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def vista_listado_alumnos2(rquest):

    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante", "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}


    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)


    return HttpResponse(documento)