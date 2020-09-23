import pytest
from django.urls import reverse

from apps.base.django_assertions import asert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_page(resp):
    asert_contains(resp, '<title>Dacio Lima Dev</title>')


def test_title_link(resp):
    asert_contains(resp, f'href="{reverse("home")}">DL-DEV</a>')
