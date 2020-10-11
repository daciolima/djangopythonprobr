import pytest
from django.urls import reverse
from apps.base.django_assertions import assert_contains


@pytest.fixture()
def resp(client):
    return client.get(reverse('aperitivo:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Luciano Ramalho OO em Python',
        'Python Set Pratice - Conjuntos'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)
#
#
# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/BwAF7ke7Px0')
