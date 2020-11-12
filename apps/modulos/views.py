from django.shortcuts import render

from apps.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}
    return render(request, 'modulos/modulo_indice.html', ctx)


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
