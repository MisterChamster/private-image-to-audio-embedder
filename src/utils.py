from os import chdir, getcwd, listdir
from src.file_operations.general import has_img_extension



def get_stripped_title(album_title):
    """
    Returns album title with everything until fist space (including) and 
    everything after last ) removed.

    Args:
        album_title (str): String to be cut.
    Returns:
        album_title (str): Cut album title.
    """
    iter = 0
    del_chars_start = 0
    del_chars_end = len(album_title)
    while iter < len(album_title):
        if album_title[iter] != " ":
            del_chars_start += 1
        else:
            del_chars_start += 1
            break
        iter += 1

    iter = len(album_title) - 1
    while iter >= 0:
        if album_title[iter] != ")":
            del_chars_end -= 1
        else:
            break
        iter -= 1

    album_title = album_title[del_chars_start:del_chars_end]
    return album_title


def get_images_list(images_dir):
    og_path = getcwd()
    chdir(images_dir)
    images_list = [node for node in listdir() if has_img_extension(node)]
    chdir(og_path)
    return images_list
