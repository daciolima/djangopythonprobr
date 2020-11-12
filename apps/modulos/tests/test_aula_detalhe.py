import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.base.django_assertions import assert_contains
from apps.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    # Criando 3 instâncias referentes ao model Aula, onde o atributo modulo tem que está conectado ao modulo
    # Visto que Aula tem chave estrangeira
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    # O reverse faz referência a App e o name na url.
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_video_youtube(resp, aula: Aula):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{ aula.youtube_id}"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')
