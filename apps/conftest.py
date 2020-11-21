# Configuração de de resp de teste com para reutilização de testes com usuario
import pytest
from model_mommy import mommy


@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_modelo = mommy.make(django_user_model, first_name='Fulano')
    return usuario_modelo


@pytest.fixture
def cliente_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client
