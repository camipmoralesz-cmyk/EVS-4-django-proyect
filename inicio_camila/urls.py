from django.urls import path, include
from . import views

app_name = 'inicio_camila'


urlpatterns = [
    path('', views.inicio, name='inicio'),
]