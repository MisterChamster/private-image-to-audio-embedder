from src.utils import Utils
from src.img_to_audio.mp3 import (has_image_mp3,
                                     embed_image_mp3,
                                     remove_image_mp3)
from src.img_to_audio.flac import (has_image_flac,
                                      embed_image_flac,
                                      remove_image_flac)



def is_image_embedded(audio_path):
    """
    Checks if audio file (mp3, flac) has image embeddec.

    Args:
        audio_path (str): Path of a audio file.

    Returns:
        bool: If audio file has image embeddec. False otherwise.
    """
    if Utils.get_extension(audio_path) == "mp3":
        return has_image_mp3(audio_path)
    elif Utils.get_extension(audio_path) == "flac":
        return has_image_flac(audio_path)


def embed_image(audio_path, image_path):
    """
    Removes, than adds an image to a mp3 or flac file.

    Args:
        audio_path (str): Path of a audio file.
        image_path (str): Path of an image.
    Returns:
        None
    """
    if Utils.get_extension(audio_path) == "mp3":
        remove_image_mp3(audio_path)
        embed_image_mp3(audio_path, image_path)
    elif Utils.get_extension(audio_path) == "flac":
        remove_image_flac(audio_path)
        embed_image_flac(audio_path, image_path)


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
