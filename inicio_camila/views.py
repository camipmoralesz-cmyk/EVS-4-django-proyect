from django.shortcuts import render
from django.http import Http404
from django.contrib.staticfiles import finders

GENEROS = [
    {
        'nombre': 'Acción',
        'descripcion': 'Persecuciones, peleas y mucha adrenalina.',
        # Esta imagen ya existe en static/css/imagenes; también sirve como referencia del género.
        'imagen': 'css/imagenes/accion1.jpg',
        'icono': 'bi bi-lightning-charge-fill',
        'peliculas': [
            {'nombre': 'Mad Max: Fury Road', 'año': 2015, 'imagen': 'imagenes/accion/accion1.jpg'},
            {'nombre': 'John Wick', 'año': 2014, 'imagen': 'imagenes/accion/accion2.jpg'},
            {'nombre': 'The Dark Knight', 'año': 2008, 'imagen': 'imagenes/accion/accion3.jpg'},
            {'nombre': 'Die Hard', 'año': 1988, 'imagen': 'imagenes/accion/accion4.jpg'},
            {'nombre': 'Gladiator', 'año': 2000, 'imagen': 'imagenes/accion/accion5.jpg'},
            {'nombre': 'The Matrix', 'año': 1999, 'imagen': 'imagenes/accion/accion6.jpg'},
            {'nombre': 'Terminator 2: Judgment Day', 'año': 1991, 'imagen': 'imagenes/accion/accion7.jpg'},
            {'nombre': 'Avengers: Endgame', 'año': 2019, 'imagen': 'imagenes/accion/accion8.jpg'},
            {'nombre': 'Inception', 'año': 2010, 'imagen': 'imagenes/accion/accion9.jpg'},
            {'nombre': 'Mission: Impossible - Fallout', 'año': 2018, 'imagen': 'imagenes/accion/accion10.jpg'}
        ]
    },
    {
        'nombre': 'Comedia',
        'descripcion': 'Películas para reír y pasar un buen rato.',
        'imagen': 'imagenes/genero/comedia.jpg',
        'icono': 'bi bi-emoji-laughing-fill',
        'peliculas': [
            {'nombre': 'Superbad', 'año': 2007, 'imagen': 'imagenes/peliculas/comedia1.jpg'},
            {'nombre': 'The Hangover', 'año': 2009, 'imagen': 'imagenes/peliculas/comedia2.jpg'},
            {'nombre': 'Step Brothers', 'año': 2008, 'imagen': 'imagenes/peliculas/comedia3.jpg'},
            {'nombre': 'Bridesmaids', 'año': 2011, 'imagen': 'imagenes/peliculas/comedia4.jpg'},
            {'nombre': 'Mean Girls', 'año': 2004, 'imagen': 'imagenes/peliculas/comedia5.jpg'},
            {'nombre': 'Dumb and Dumber', 'año': 1994, 'imagen': 'imagenes/peliculas/comedia6.jpg'},
            {'nombre': 'Groundhog Day', 'año': 1993, 'imagen': 'imagenes/peliculas/comedia7.jpg'},
            {'nombre': 'Anchorman', 'año': 2004, 'imagen': 'imagenes/peliculas/comedia8.jpg'},
            {'nombre': 'Shaun of the Dead', 'año': 2004, 'imagen': 'imagenes/peliculas/comedia9.jpg'},
            {'nombre': 'Tropic Thunder', 'año': 2008, 'imagen': 'imagenes/peliculas/comedia10.jpg'}
        ]
    },
    {
        'nombre': 'Romance',
        'descripcion': 'Películas de amor y relaciones románticas.',
        'imagen': 'imagenes/genero/romance.jpg',
        'icono': 'bi bi-heart-fill',
        'peliculas': [
            {'nombre': 'The Notebook', 'año': 2004, 'imagen': 'imagenes/romance/romance1.jpg'},
            {'nombre': 'Pride & Prejudice', 'año': 2005, 'imagen': 'imagenes/romance/romance2.jpg'},
            {'nombre': 'Titanic', 'año': 1997, 'imagen': 'imagenes/romance/romance3.jpg'},
            {'nombre': 'La La Land', 'año': 2016, 'imagen': 'imagenes/romance/romance4.jpg'},
            {'nombre': 'Before Sunrise', 'año': 1995, 'imagen': 'imagenes/romance/romance5.jpg'},
            {'nombre': '10 Things I Hate About You', 'año': 1999, 'imagen': 'imagenes/romance/romance6.jpg'},
            {'nombre': 'Notting Hill', 'año': 1999, 'imagen': 'imagenes/romance/romance7.jpg'},
            {'nombre': 'A Walk to Remember', 'año': 2002, 'imagen': 'imagenes/romance/romance8.jpg'},
            {'nombre': 'Me Before You', 'año': 2016, 'imagen': 'imagenes/romance/romance9.jpg'},
            {'nombre': 'About Time', 'año': 2013, 'imagen': 'imagenes/romance/romance10.jpg'}
        ]
    },
    {
        'nombre': 'Terror',
        'descripcion': 'Películas que no te dejarán dormir en la noche.',
        'imagen': 'imagenes/genero/terror.jpg',
        'icono': 'bi bi-eye-fill',
        'peliculas': [
            {'nombre': 'The Exorcist', 'año': 1973, 'imagen': 'imagenes/terror/terror1.jpg'},
            {'nombre': 'The Shining', 'año': 1980, 'imagen': 'imagenes/terror/terror2.jpg'},
            {'nombre': 'A Nightmare on Elm Street', 'año': 1984, 'imagen': 'imagenes/terror/terror3.jpg'},
            {'nombre': 'Halloween', 'año': 1978, 'imagen': 'imagenes/terror/terror4.jpg'},
            {'nombre': 'Get Out', 'año': 2017, 'imagen': 'imagenes/terror/terror5.jpg'},
            {'nombre': 'Hereditary', 'año': 2018, 'imagen': 'imagenes/terror/terror6.jpg'},
            {'nombre': 'The Conjuring', 'año': 2013, 'imagen': 'imagenes/terror/terror7.jpg'},
            {'nombre': 'It', 'año': 2017, 'imagen': 'imagenes/terror/terror8.jpg'},
            {'nombre': 'Scream', 'año': 1996, 'imagen': 'imagenes/terror/terror9.jpg'},
            {'nombre': 'A Quiet Place', 'año': 2018, 'imagen': 'imagenes/terror/terror10.jpg'}
        ]
    }
]


def _preparar_imagenes(genero):
    """Marca qué imágenes existen para evitar enlaces rotos en las plantillas."""
    return {
        **genero,
        'imagen_disponible': bool(genero['imagen'] and finders.find(genero['imagen'])),
        'peliculas': [
            {
                **pelicula,
                'imagen_disponible': bool(
                    pelicula['imagen'] and finders.find(pelicula['imagen'])
                ),
            }
            for pelicula in genero['peliculas']
        ],
    }


def inicio(request):
    generos = [_preparar_imagenes(genero) for genero in GENEROS]
    return render(request, 'inicio_camila/inicio.html', {'generos': generos})

def genero(request, nombre):
    seleccionado = next((genero for genero in GENEROS if genero['nombre'] == nombre), None)
    if seleccionado is None:
        raise Http404('Género no encontrado')
    return render(request, 'genero.html', {'genero': _preparar_imagenes(seleccionado)})