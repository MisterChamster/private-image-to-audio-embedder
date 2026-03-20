from pathlib import Path



class Utils():
    @staticmethod
    def is_img_file(file_path: Path) -> bool:
        extension = file_path.suffix
        audio_exts = ("png", "jpg", "jpeg")

        if extension in audio_exts:
            return True
        return False


    @staticmethod
    def is_audio_file(file_path: Path) -> bool:
        extension = file_path.suffix
        audio_exts = ("mp3", "flac")

        if extension in audio_exts:
            return True
        return False


    @staticmethod
    def get_dirs_from_dir(dir_path: Path) -> list[Path]:
        """
        Returns a list of directories in current working directory.

        Returns:
            dirs_in_dir (Path): Names of directories in current working directory.
        """
        dirs_in_dir = [node
                       for node in dir_path.iterdir()
                       if node.is_dir()]
        return dirs_in_dir


    @staticmethod
    def get_images_list(dir_path: Path) -> list[Path]:
        images_list = [node
                       for node in dir_path.iterdir()
                       if Utils.is_img_file(node)]
        return images_list


    @staticmethod
    def get_audios_from_dir(dir_path: Path) -> list[Path]:
        """
        Returns a list of mp3 and flac files in current working directory.

        Returns:
            list (Path): Names of mp3 and flac files in current working directory.
        """
        audios_in_dir = [node
                         for node in dir_path.iterdir()
                         if Utils.is_audio_file(node)]
        return audios_in_dir


    @staticmethod
    def strip_title(album_title: str) -> str:
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
