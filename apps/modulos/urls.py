from django.urls import path
from apps.modulos.views import indice, detalhe, aula

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),
    path('aula/<slug:slug>', aula, name='aula'),
    path('', indice, name='indice'),
]
