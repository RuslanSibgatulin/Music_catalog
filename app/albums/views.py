from rest_framework import generics
from .models import Song, Singer, Album
from .serializers import SongSerializer, SingerSerializer, AlbumSerializer
from rest_framework.filters import SearchFilter


class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all().order_by("name")
    serializer_class = SongSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", ]


class SingerListAPIView(generics.ListAPIView):
    queryset = Singer.objects.all().order_by("name")
    serializer_class = SingerSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", ]


class AlbumListAPIView(generics.ListAPIView):
    queryset = Album.objects.all().order_by("name")
    serializer_class = AlbumSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "singer__name", "release_at"]
