from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Album, Singer, Song
from .serializers import AlbumSerializer, SingerSerializer, SongSerializer


class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all().order_by("name")
    serializer_class = SongSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class SingerListAPIView(generics.ListAPIView):
    queryset = Singer.objects.all().order_by("name")
    serializer_class = SingerSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class AlbumListAPIView(generics.ListAPIView):
    queryset = Album.objects.all().order_by("name")
    serializer_class = AlbumSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name", "singer__name", "release_at"]
