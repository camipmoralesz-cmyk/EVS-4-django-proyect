from django.test import TestCase
from django.urls import reverse


class InicioViewTests(TestCase):
    def test_inicio_renders_with_genres_and_valid_links(self):
        response = self.client.get(reverse('inicio_camila:inicio'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Elige un género')
        self.assertContains(response, reverse('inicio_camila:genero', args=['Acción']))

    def test_genero_renders_selected_genre(self):
        response = self.client.get(reverse('inicio_camila:genero', args=['Acción']))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Persecuciones, peleas y mucha adrenalina.')
        self.assertContains(response, 'Mad Max: Fury Road')
        self.assertContains(response, '2015')
        self.assertContains(response, '/static/imagenes/accion/accion1.jpg')

    def test_unknown_genre_returns_not_found(self):
        response = self.client.get(reverse('inicio_camila:genero', args=['Drama']))

        self.assertEqual(response.status_code, 404)

    def test_missing_poster_shows_placeholder_instead_of_broken_image(self):
        response = self.client.get(reverse('inicio_camila:genero', args=['Comedia']))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Póster aún no disponible')
        self.assertNotContains(response, '/static/imagenes/peliculas/comedia1.jpg')
