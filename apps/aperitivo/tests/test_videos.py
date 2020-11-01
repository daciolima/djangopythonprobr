import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.aperitivo.models import Video
from apps.base.django_assertions import assert_contains


@pytest.fixture
def video(db):  # o parametro db permite o pytest tesr acesso aos modelos
    return mommy.make(Video)
    # vi = Video(slug='motivacao', titulo='Luciano Ramalho OO em Python', youtube_id='BwAF7ke7Px0')
    # vi.save()
    # return vi


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivo:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivo:video', args=(video.slug + 'video_nao_existente',)))


# Testando
def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp, resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video.youtube_id}')