# Generated by Django 4.2.1 on 2023-07-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_playlist_remove_song_album_userrating_songplaylist_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]
