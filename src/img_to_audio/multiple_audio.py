from os import path, chdir, getcwd
from src.utils import (get_audios_from_cwd,
                       get_dirs_from_cwd,
                       remove_extension)
from src.img_to_audio.general_audio import (embed_image,
                                    remove_image)
from src.utils import (get_images_list,
                       get_stripped_title)



def embed_to_all_audios(audio_dir, image_path):
    """
    Adds an image to all mp3 and flac files inside a directory.

    Args:
        album_dir  (str): Path of a directory containing audio files.
        image_path (str): Path of an image to embed.
    Returns:
        None
    """
    og_path = getcwd()
    chdir(audio_dir)
    songs_in_cd = get_audios_from_cwd()
    chdir(og_path)
    for audiofile in songs_in_cd:
        embed_image(audio_dir + "/" + audiofile, image_path)


def img_dir_to_audio_file(audio_path, images_dir):
    images_list = get_images_list(images_dir)

    index = 0
    print(audio_path)
    audiofile_name = path.basename(audio_path)
    audiofile_name_no_ext = remove_extension(audiofile_name)

    while index < len(images_list):
        if audiofile_name_no_ext == remove_extension(images_list[index]):
            print(audiofile_name)
            embed_image(audio_path, images_dir + "/" + images_list[index])
            images_list.pop(index)          ###### Picture can't be embedded to another album
            break
        index += 1


def img_dir_to_audio_dir(audio_dir, images_dir):
    OGpath = getcwd()
    chdir(audio_dir)

    images_list = get_images_list(images_dir)
    index = 0
    cwd_name = get_stripped_title(path.basename(getcwd()))
    #lowercase for better name matching
    cwd_name_lowered = cwd_name.lower()

    while index < len(images_list):
        if cwd_name_lowered == remove_extension(images_list[index].lower()):
            print(cwd_name)
            embed_to_all_audios(getcwd(), images_dir + "/" + images_list[index])
            break
        index += 1

    chdir(OGpath)


def remove_images_dir(dir_path):
    og_path = getcwd()
    chdir(dir_path)
    audios_list = get_audios_from_cwd()

    for audio in audios_list:
        remove_image(getcwd() + "/" + audio)

    chdir(og_path)


def remove_images_recursion(dir_path):
    """
    Removes images embedded to mp3 and flac files present in a directory and 
    all the directories inside.

    Args:
        dir_path (str): Path of a directory.
    Returns:
        None
    """
    og_path = getcwd()
    chdir(dir_path)
    audios_list = get_audios_from_cwd()

    for audio in audios_list:
        remove_image(getcwd() + "/" + audio)

    dirs_in_cwd = get_dirs_from_cwd()
    for direct in dirs_in_cwd:
        remove_images_recursion(direct)

    chdir(og_path)


# The recursive function doesn't change names of audiofiles in cwd and instead 
# has a function that changes is separately, because there would be a 
# significant time loss
