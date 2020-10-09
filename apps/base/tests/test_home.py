import pytest
from django.urls import reverse

from apps.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_page(resp):

    assert_contains(resp, '<title>Dacio Lima - Home</title>')



def test_title_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">DL-DEV</a>')
