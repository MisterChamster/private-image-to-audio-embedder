from os import chdir, getcwd, listdir
from os import path, listdir
from pathlib import Path



class Utils():
    @staticmethod
    def is_img_file(filename: str) -> bool:
        return filename.lower().endswith(("png", "jpg", "jpeg"))


    @staticmethod
    def is_audio_file(filename: str) -> bool:
        return filename.lower().endswith(("mp3", "flac"))


    @staticmethod
    def get_extension(filename: str) -> str:
        return Path(filename).suffix.lstrip(".")


    @staticmethod
    def remove_extension(filename: str) -> str:
        return str(Path(filename).with_suffix(""))


    @staticmethod
    def get_audios_from_cwd() -> list[str]:
        """
        Returns a list of mp3 and flac files in current working directory.

        Returns:
            list (str): Names of mp3 and flac files in current working directory.
        """
        audios_in_cwd = []
        for node in listdir():
            if Utils.is_audio_file(node):
                audios_in_cwd.append(node)
        return audios_in_cwd


    @staticmethod
    def get_dirs_from_cwd() -> list[str]:
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


    @staticmethod
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


    @staticmethod
    def get_images_list(images_dir):
        og_path = getcwd()
        chdir(images_dir)
        images_list = [node for node in listdir() if Utils.is_img_file(node)]
        chdir(og_path)
        return images_list
