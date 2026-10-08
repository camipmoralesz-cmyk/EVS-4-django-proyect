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

    def test_unknown_genre_returns_not_found(self):
        response = self.client.get(reverse('inicio_camila:genero', args=['Drama']))

        self.assertEqual(response.status_code, 404)
