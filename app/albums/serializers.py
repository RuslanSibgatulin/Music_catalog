from rest_framework import serializers

from .models import Song, Singer, Album


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = "__all__"
