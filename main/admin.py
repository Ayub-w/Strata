from django.contrib import admin
from .models import song, album, songplaylist, userRating, playlist

# Register your models here.
admin.site.register(song)
admin.site.register(album)
admin.site.register(songplaylist)
admin.site.register(userRating)
admin.site.register(playlist)