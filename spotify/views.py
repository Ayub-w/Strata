from django.shortcuts import render
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from main.views import home_view
from requests import Request, post
from rest_framework import status
from rest_framework import response


# Create your views here.


class AuthURL(home_view):
    def get(self, request, fornat=None):
        scopes = 'user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative '

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return response({'url': url}, status=status.HTTP_200_OK)
