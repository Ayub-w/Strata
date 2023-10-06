from mutagen.mp3 import MP3
from django.core.exceptions import ValidationError
import os

def validate_is_mp3(file):
    try:
        audio = MP3(file)
        if not audio:
            raise TypeError()
        first_file_check = True
    except Exception as e:
        first_file_check = False
    if not first_file_check:
        raise ValidationError("File is not an mp3")
    valid_file_extensions = ['.mp3']
    ext = os.path.splitext(file.name)[1]
    if not ext.lower() in valid_file_extensions:
        raise ValidationError("Unsupported file extension.")