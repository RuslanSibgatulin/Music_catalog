from django.urls import path

from .views import AlbumListAPIView, SingerListAPIView, SongListAPIView

app_name = "albums_api"

urlpatterns = [
    path("songs/", SongListAPIView.as_view()),
    path("singers/", SingerListAPIView.as_view()),
    path("albums/", AlbumListAPIView.as_view()),
]
