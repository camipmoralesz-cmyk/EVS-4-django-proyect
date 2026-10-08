from django.shortcuts import render
from django.http import Http404


GENEROS = [
    {'nombre': 'Acción', 'descripcion': 'Persecuciones, peleas y mucha adrenalina.'},
    {'nombre': 'Comedia', 'descripcion': 'Películas para reír y pasar un buen rato.'},
]

def inicio(request):
    return render(request, 'inicio_camila/inicio.html', {'generos': GENEROS})

def genero(request, nombre):
    seleccionado = next((genero for genero in GENEROS if genero['nombre'] == nombre), None)
    if seleccionado is None:
        raise Http404('Género no encontrado')
    return render(request, 'genero.html', {'genero': seleccionado})
