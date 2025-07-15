from os import path, chdir, listdir, getcwd
from src.file_operations.general import get_audios_from_cwd
from src.file_operations.audio import embed_image



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
