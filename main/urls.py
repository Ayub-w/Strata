from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.home_view, name="home")
    #path("login/", views.login, name="login"),
    #path("register/", views.register, name="register"),
    #path("playlist/", views.playlist, name="playlist"),
    #path("logout/", views.logout, name="logout"),
]