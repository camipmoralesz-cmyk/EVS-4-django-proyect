from django.shortcuts import render

def inicio(request):
    generos = [
        {'nombre': 'Acción', 'descripcion': '...'},
        {'nombre': 'Comedia', 'descripcion': '...'},
    ]
    return render(request, 'inicio_camila/inicio.html', {'generos': generos})

def genero(request, nombre):
    peliculas = []  # aquí irán las 10 películas
    return render(request, 'inicio_camila/genero.html', {'nombre': nombre, 'peliculas': peliculas})