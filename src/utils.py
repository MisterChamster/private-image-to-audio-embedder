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
