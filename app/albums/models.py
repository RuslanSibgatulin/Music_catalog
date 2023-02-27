from django.db import models
from django.utils.translation import gettext_lazy as _


class NameMixin(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name}"


class Singer(NameMixin):

    class Meta:
        verbose_name = _("Singer")
        verbose_name_plural = _("Singers")


class Song(NameMixin):

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")


class Album(NameMixin):
    singer = models.ForeignKey(
        Singer,
        on_delete=models.PROTECT,
        verbose_name=_("Singer"),
    )
    release_at = models.DateField(_("Release"))
    songs = models.ManyToManyField(
        Song,
        through="SongsInAlbum",
        verbose_name=_("Songs")
    )


class SongsInAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    number = models.PositiveSmallIntegerField(_("Sequence number"))

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["album", "song"],
                name="songs_in_album_idx"),
            models.UniqueConstraint(
                fields=["album", "number"],
                name="number_in_album_idx")
        ]
