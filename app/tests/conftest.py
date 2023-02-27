import pytest
from rest_framework.test import APIClient

API_URL = "http://127.0.0.1:8000/api/v1/"


@pytest.fixture
def api_url():
    return API_URL


@pytest.fixture
def client():
    api_client = APIClient()
    return api_client


@pytest.fixture
def song():
    from albums.models import Song
    return Song.objects.create(name="Song 1")


@pytest.fixture
def singer():
    from albums.models import Singer
    return Singer.objects.create(name="Singer 1")


@pytest.fixture
def album(singer, song):
    from albums.models import Album
    album = Album.objects.create(
        name="Album 1",
        singer=singer,
        release_at="2000-01-01",
    )
    album.songs.set([song], through_defaults={"number": 1})
    return album
