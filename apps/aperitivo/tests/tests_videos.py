import pytest
from django.urls import reverse
from apps.base.django_assertions import assert_contains


@pytest.fixture()
def resp(client):
    return client.get(reverse('aperitivo:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Luciano Ramalho OO em Python</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/BwAF7ke7Px0')
