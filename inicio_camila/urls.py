from django.urls import path
from . import views

app_name = 'inicio_camila'


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<str:nombre>/', views.genero, name='genero'),
]