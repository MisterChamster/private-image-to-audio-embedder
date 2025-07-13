# from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC, Picture
from mutagen.id3 import ID3, APIC, error
from os import path, chdir, listdir, getcwd
from src.file_operations.general import (has_img_extension,
                                         get_extension,
                                         remove_extension)
from src.file_operations.mp3 import (has_image_mp3,
                                     embed_image_mp3,
                                     remove_image_mp3)
from src.file_operations.flac import (has_image_flac,
                                      embed_image_flac,
                                      remove_image_flac)



def has_image_audio(audio_path):
    """
    Checks if audio file (mp3, flac) has image embeddec.

    Args:
        audio_path (str): Path of a audio file.

    Returns:
        bool: If audio file has image embeddec. False otherwise.
    """
    if get_extension(audio_path) == "mp3":
        return has_image_mp3(audio_path)
    elif get_extension(audio_path) == "flac":
        return has_image_flac(audio_path)


def remove_image(audio_path):
    """
    Removes an embedded image from mp3 or flac file.

    Args:
        audio_path (str): Path of the audio file.
    Returns:
        None
    """
    if audio_path.endswith(".mp3"):
        remove_image_mp3(audio_path)
    elif audio_path.endswith(".flac"):
        remove_image_flac(audio_path)
