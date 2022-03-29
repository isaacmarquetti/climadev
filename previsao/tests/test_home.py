import pytest
from django.urls import reverse
from climaapi.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('home'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_example():
    assert 1 == 1


def test_title(resp):
    assert_contains(resp, '<title>Consulta Clima-DEV</title>')


