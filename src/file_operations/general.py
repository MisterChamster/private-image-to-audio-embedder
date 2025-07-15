from os import path, listdir



def has_img_extension(filename):
    if (filename.endswith("png") or
        filename.endswith("jpg") or
        filename.endswith("jpeg")):
        return True
    return False


def get_extension(filename):
    return filename.split(".")[-1]


def remove_extension(filename):
    """
    Removes extension (characters from ending until last dot, included)

    Args:
        filename (str): String that will be cut.
    Returns:
        filename (str): String with extension removed.
    """
    dot_list = filename.split(".")[:-1]
    filename = ".".join(dot_list)
    return filename


def get_audios_from_cwd():
    """
    Returns a list of mp3 and flac files in current working directory.

    Returns:
        list (str): Names of mp3 and flac files in current working directory.
    """
    audios_in_cwd = []
    for node in listdir():
        if get_extension(node) == "mp3" or get_extension(node) == "flac":
            audios_in_cwd.append(node)
    return audios_in_cwd


def get_dirs_from_cwd():
    """
    Returns a list of directories in current working directory.

    Returns:
        dirs_in_cwd (str): Names of directories in current working directory.
    """
    dirs_in_cwd = []
    for node in listdir():
        if path.isdir(node):
            dirs_in_cwd.append(node)
    return dirs_in_cwd
