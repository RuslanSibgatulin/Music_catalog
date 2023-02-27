from http import HTTPStatus
import pytest

from rest_framework.test import APIClient
from albums.models import Song, Singer, Album


@pytest.mark.django_db
def test_get_songs(client: APIClient, api_url: str, song: Song):
    url = api_url + "songs/"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["count"] == 1


@pytest.mark.django_db
def test_get_singers(client: APIClient, api_url: str, singer: Singer):
    url = api_url + "singers/"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["count"] == 1


@pytest.mark.django_db
def test_get_albums(client: APIClient, api_url: str, album: Album):
    url = api_url + "albums/"
    response = client.get(url)
    print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert response.json()["count"] == 1
    album = response.json()["results"][0]
    assert album["name"] == "Album 1"
    assert album["release_at"] == "2000-01-01"
