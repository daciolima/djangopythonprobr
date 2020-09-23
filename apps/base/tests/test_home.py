from django.test import Client

from apps.base.django_assertions import asert_contains


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_title_page(client: Client):
    resp = client.get('/')
    asert_contains(resp, '<title>Dácio Lima Dev</title>')

