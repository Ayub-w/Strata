from django.shortcuts import render
from django.http import HttpResponse
from main.models import song
from main.models import playlist


# Create your views here.

def player(request):
    songs = song.objects.all()
    song_list = list(song.objects.all().values())
    return render(request, "pages/player.html", {
        'songs': songs,
        'song_list': song_list,
    })
def home_view(request):

    return render(request, "pages/home.html", {})



def login(response):
    return render(response, "registration/login.html", {})

def register(response):
    return render(response, "registration/register.html", {})

def playlist(request):
    playlists = playlist.objects.all()
    playlist_list = list(playlist.objects.all().values())
    return render(request, "pages/playlist.html", {
        'playlists': playlists,
        'playlist_list': playlist_list,
    })
