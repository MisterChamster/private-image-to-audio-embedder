def has_img_extension(filename):
    """
    Checks if file has jpg, png or jpeg extension.

    Args:
        filename (str): Name of a file.
    Returns:
        (boolean): If file is an image or not.
    """
    if filename[-3:] in ["png", "jpg"] or filename.endswith("jpeg"):
        return True
    return False


def get_extension(filename):
    """
    Returns extension of a file.
    
    Args:
        filename (str): Name of a file from which extension will be got.
    Returns:
        ext (str): File extension.
    """
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
