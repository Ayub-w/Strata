from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.home_view, name="home"),
    path('login/', views.login, name="login"),
    path('', include('members.urls')),
    path('admin/', include(admin.site.urls)),
    path('', views.player, name="player"),
    #path("register/", views.register, name="register"),
    #path("playlist/", views.playlist, name="playlist"),
    #path("logout/", views.logout, name="logout"),
]