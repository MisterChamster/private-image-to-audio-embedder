from pathlib import Path



class Utils():
    @staticmethod
    def is_img_file(file_path: Path) -> bool:
        extension = file_path.suffix
        audio_exts = (".png", ".jpg", ".jpeg")

        if extension in audio_exts:
            return True
        return False


    @staticmethod
    def is_audio_file(file_path: Path) -> bool:
        extension = file_path.suffix
        audio_exts = (".mp3", ".flac", ".ogg")

        if extension in audio_exts:
            return True
        return False


    @staticmethod
    def get_dirs_from_dir(dir_path: Path) -> list[Path]:
        dirs_in_dir = [node
                       for node in dir_path.iterdir()
                       if node.is_dir()]
        dirs_in_dir.sort()
        return dirs_in_dir


    @staticmethod
    def get_images_list(dir_path: Path) -> list[Path]:
        images_list = [node
                       for node in dir_path.iterdir()
                       if Utils.is_img_file(node)]
        images_list.sort()
        return images_list


    @staticmethod
    def get_audios_from_dir(dir_path: Path) -> list[Path]:
        audios_in_dir = [
            node
            for node in dir_path.iterdir()
            if Utils.is_audio_file(node)]
        audios_in_dir.sort()
        return audios_in_dir


    @staticmethod
    def strip_title(album_title: str) -> str:
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
