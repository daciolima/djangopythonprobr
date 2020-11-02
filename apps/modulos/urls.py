from django.urls import path
from apps.aperitivo.views import video, indice
from apps.modulos.views import detalhe

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),

]

