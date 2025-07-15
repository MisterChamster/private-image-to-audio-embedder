from os import path, chdir, listdir, getcwd
from src.file_operations.general import (get_audios_from_cwd,
                                         get_dirs_from_cwd)
from src.file_operations.audio import (embed_image,
                                       remove_image)



def embed_to_all_audios(audio_dir, image_path):
    """
    Adds an image to all mp3 and flac files inside a directory.

    Args:
        album_dir  (str): Path of a directory containing audio files.
        image_path (str): Path of an image to embed.
    Returns:
        None
    """
    OGpath = getcwd()
    chdir(audio_dir)
    songs_in_cd = get_audios_from_cwd()
    chdir(OGpath)
    for audiofile in songs_in_cd:
        embed_image(audio_dir + "/" + audiofile, image_path)


def remove_images_recursion(dir_path):
    """
    Removes images embedded to mp3 and flac files present in a directory and 
    all the directories inside.

    Args:
        dir_path (str): Path of a directory.
    Returns:
        None
    """
    OGpath = getcwd()
    chdir(dir_path)
    audios_list = get_audios_from_cwd()

    for audio in audios_list:
        remove_image(getcwd() + "/" + audio)

    dirs_in_cwd = get_dirs_from_cwd()
    for direct in dirs_in_cwd:
        remove_images_recursion(direct)

    chdir(OGpath)
