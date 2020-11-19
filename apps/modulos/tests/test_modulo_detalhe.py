import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.base.django_assertions import assert_contains
from apps.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aulas(modulo):
    # Criando 3 instâncias referentes ao model Aula, onde o atributo modulo tem que está conectado ao modulo
    # Visto que Aula tem chave estrangeira
    return mommy.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo, aulas):
    # O reverse faz referência a App e o name na url.
    resp = client.get(reverse("modulos:detalhe", kwargs={"slug": modulo.slug}))
    return resp


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_aulas_titulos(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_links(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
