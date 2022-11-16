from django.urls import path
from appUNO.views import *


urlpatterns = [
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("cursos/", cursos),
    path("entregables/", entregables),

]
