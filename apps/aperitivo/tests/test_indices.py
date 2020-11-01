import pytest
from django.urls import reverse
from model_mommy import mommy

from apps.aperitivo.models import Video
from apps.base.django_assertions import assert_contains


@pytest.fixture
def videos(db):  # o parametro db permite o pytest tesr acesso aos modelos
    return mommy.make(Video, 3)


@pytest.fixture()
def resp(client, videos):
    return client.get(reverse('aperitivo:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


#
# @pytest.mark.parametrize(
#     'titulo',
#     [
#         'Luciano Ramalho OO em Python',
#         'Python Set Pratice - Conjuntos'
#     ]
# )


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


# @pytest.mark.parametrize(
#     'slug',
#     [
#         'motivacao',
#         'instalacao-windows'
#     ]
# )
def test_link_video(resp, videos):
    for video in videos:
        video_link = reverse('aperitivo:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
