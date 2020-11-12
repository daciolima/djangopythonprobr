from typing import List

from django.db.models import Prefetch

from apps.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por título
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_modulos_ordenados(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    # O método select_related() carrega de uma vez o modulo em questão evitando várias
    # query ao banco(N+1). Nesse processo ele faz um INNER_JOIN.
    # OBS: Ele só funciona quando estamos do lado N para acessar o lado 1.
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    aulas_ordenadas = Aula.objects.order_by('order')
    # O método prefetch_related() faz um query buscando o o lado 1, depois uma query para buscar as aulas,
    # E o JOIN é feito pelo python/ORM;
    # OBS: Ele funciona quando estamos do lado 1 para acessar o lado N.
    # Queryset pega uma query customizada e gera uma lista conforme o parametro de to_attr=''
    # No exemplo abaixo foi usada no template modulos/modulo_indice.html
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')).all()
