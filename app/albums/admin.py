from django.contrib import admin

from .models import Album, Singer, Song, SongsInAlbum


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("name", )

    # Поиск по полям
    search_fields = ("name", )


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ("name", )

    # Поиск по полям
    search_fields = ("name", )


class SongAlbumInline(admin.TabularInline):
    model = SongsInAlbum


@admin.register(Album)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (SongAlbumInline, )

    # Отображение полей в списке
    list_display = ("name", "singer", "release_at")

    # Поиск по полям
    search_fields = ("name", "singer")

    # Фильтрация в списке
    list_filter = ("release_at", )
