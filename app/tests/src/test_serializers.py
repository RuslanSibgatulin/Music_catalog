from albums.serializers import (AlbumSerializer, SingerSerializer,
                                SongSerializer)


def test_SongSerializer():
    serializer = SongSerializer()
    assert set(serializer.get_fields()) == {"id", "name"}


def test_SingerSerializer():
    serializer = SingerSerializer()
    assert set(serializer.get_fields()) == {"id", "name"}


def test_AlbumSerializer():
    serializer = AlbumSerializer()
    assert set(serializer.get_fields()) == {
        "id", "name", "release_at", "singer", "songs",
    }
