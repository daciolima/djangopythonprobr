import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.base.django_assertions import assert_contains
from apps.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)
