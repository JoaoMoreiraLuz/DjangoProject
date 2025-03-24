#Test for the post view
import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    # Checando o status code da resposta
    assert response.status_code == 200

    # Checando o conteudo da resposta
    assert response.content == b'Hello, world!'