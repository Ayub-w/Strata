from django.db import models
from main.helpers import get_mp3_length
from main.validator import validate_is_mp3

# Create your models here.

class song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.ManyToManyField( 'album', related_name="+", blank=True)
    genre = models.CharField(max_length=100)
    duration = models.DecimalField(blank=True, max_digits=15, decimal_places=2)
    cover_image = models.ImageField(upload_to='images/')
    audiofile = models.FileField(upload_to='main/static/player/', validators=[validate_is_mp3])
    def save(self, *args, **kwargs):
        if not self.duration:
            # get the duration of the mp3 file
            mp3_length = get_mp3_length(self.audiofile)
            self.duration = f'{mp3_length:.2f}'
        return super().save(*args, **kwargs)
    class Meta:
        ordering = ['title']


class album(models.Model):
    albumTitle = models.CharField(max_length=100)
    songlist = models.ManyToManyField(song, related_name="+", blank=True)
    albumArtist = models.CharField(max_length=100)
    albumYear = models.IntegerField()
    albumGenre = models.CharField(max_length=100)
    albumImage = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.albumTitle

class songplaylist(models.Model):
    songPlaylistID = models.IntegerField()
    songPlaylistName = models.CharField(max_length=100)
    songPlaylistSongs = models.ManyToManyField(song, related_name="+", blank=True)
    user = models.ForeignKey('auth.User', related_name="+", on_delete=models.CASCADE, blank=True)
    playlistID = models.ForeignKey('playlist', related_name="+", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.playlistName
class userRating(models.Model):
    userID = models.ForeignKey( 'auth.User', related_name="+", on_delete=models.CASCADE, blank=True)
    songID = models.IntegerField()
    rating = models.IntegerField()
    listen_count = models.IntegerField()

    def __str__(self):
        return self.rating
class playlist(models.Model):
    playlistID = models.IntegerField()
    playlistName = models.CharField(max_length=100)
    playlistSongs = models.ManyToManyField(song, related_name="+", blank=True)
    created_date = models.DateField(null=True)
    user = models.ForeignKey('auth.User', related_name="+", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.playlistName