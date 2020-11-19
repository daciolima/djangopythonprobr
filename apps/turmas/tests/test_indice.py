import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):  # Criando uma relação com a App e o name do link para ser usada nos testes
    return client.get(reverse('turmas:indice'))


def test_status_code(resp):
    assert resp.status_code == 200
