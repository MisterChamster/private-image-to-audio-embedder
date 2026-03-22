from pathlib import Path

from src.utils import Utils
from src.img_to_audio.audio_file_tools import AudioFileTools



class AudioDirTools():
    @staticmethod
    def embed_img_file_to_audio_dir(audio_dir_path: Path, image_path: Path) -> None:
        """
        Embeds an image to all mp3 and flac files inside a directory.

        Args:
            album_dir  (str): Path of a directory containing audio files.
            image_path (str): Path of an image to embed.
        Returns:
            None
        """
        audio_file_paths = Utils.get_audios_from_dir(audio_dir_path)

        for audio_path in audio_file_paths:
            AudioFileTools.embed_image_safe(
                audio_path,
                image_path)


    @staticmethod
    def embed_img_dir_to_audio_file(audio_path: Path, images_dir_path: Path) -> None:
        print(audio_path)

        images_paths    = Utils.get_images_list(images_dir_path)
        audio_file_name = audio_path.name
        audio_name      = audio_path.stem

        index = 0
        while index < len(images_paths):
            image_path = images_paths[index]
            image_name = image_path.stem

            if audio_name == image_name:
                print(audio_file_name)
                AudioFileTools.embed_image_safe(
                    audio_path,
                    image_path)

                # Picture can't be embedded to another album
                images_paths.pop(index)
                break
            index += 1


    @staticmethod
    def embed_img_dir_to_audio_dir(audio_dir_path: Path, images_dir_path: Path) -> None:
        images_list = Utils.get_images_list(images_dir_path)
        dir_name    = Utils.strip_title(audio_dir_path.name)
        #lowercase for better name matching
        dir_name_lowered = dir_name.lower()

        index = 0
        while index < len(images_list):
            image_path = images_list[index]
            image_name_lowered = image_path.stem.lower()

            if dir_name_lowered == image_name_lowered:
                print(dir_name)
                AudioDirTools.embed_img_file_to_audio_dir(
                    audio_dir_path,
                    image_path)
                break
            index += 1


    @staticmethod
    def remove_images_dir(dir_path: Path) -> None:
        audios_list = Utils.get_audios_from_dir(dir_path)

        for audio_path in audios_list:
            AudioFileTools.remove_image(audio_path)


    @staticmethod
    def remove_images_recursion(dir_path: Path) -> None:
        """
        Removes images embedded to mp3 and flac files present in a directory and
        all the directories inside.

        Args:
            dir_path (str): Path of a directory.
        Returns:
            None
        """
        audios_list = Utils.get_audios_from_dir(dir_path)
        dirs_in_dir = Utils.get_dirs_from_dir(dir_path)

        for audio_path in audios_list:
            AudioFileTools.remove_image(audio_path)

        for direct in dirs_in_dir:
            AudioDirTools.remove_images_recursion(direct)



    # The recursive function doesn't change names of audiofiles in
    # dir_path and instead has a function that changes is separately,
    # because there would be a significant time loss
