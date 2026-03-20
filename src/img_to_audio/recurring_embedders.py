from os import path, chdir
from pathlib import Path

from src.utils import Utils
from src.img_to_audio.audio_dir_tools  import AudioDirTools
from src.img_to_audio.audio_file_tools import AudioFileTools



class RecurringEmbedders():
    images_dir_path: Path
    images_list:     list[str]

    def __init__(self, images_dir_path: Path):
        self.images_dir_path = images_dir_path
        self.images_list = Utils.get_images_list(images_dir_path)


    def embed_images_recursion_conditional(self, audio_dir: Path) -> None:
        """
        Recursively attributes images to songs.

        Function working order:
            1. If name of audio_dir is in images list,
            attribute image of this name to all audio files inside.
            2. If it's not, check if names of any audio files in audio_dir
            match names of images in image list and attribute accordingly.
            3. Recur in every directory inside audio_dir.

        Args:
            audio_dir (str): Path of audio directory.
        Returns:
            None
        """
        # Check if all songs have embedded image
        index = 0
        not_all_songs_embedded = False
        audio_paths = Utils.get_audios_from_dir(audio_dir)

        while index < len(audio_paths):
            audio_dir_path = audio_paths[index]
            is_embedded = AudioFileTools.is_image_embedded(audio_dir_path)
            if not is_embedded:
                not_all_songs_embedded = True
                break
            index += 1

        #Check based on current directory name and image name
        did_attribute = False
        audio_dir_name = Utils.strip_title(audio_dir.stem)
        #lowercase for better name matching
        audio_dir_name_lowered = audio_dir_name.lower()

        if not_all_songs_embedded:
            index = 0
            while index < len(self.images_list):

                if audio_dir_name_lowered == Utils.remove_extension(self.images_list[index].lower()):
                    print(audio_dir_name)
                    image_path = self.images_dir_path / self.images_list[index]
                    AudioDirTools.embed_img_file_to_audio_dir(
                        audio_dir,
                        image_path)
                    # Picture can't be attributed to another album
                    self.images_list.pop(index)
                    did_attribute = True
                    break
                index += 1

        #THIS PROBABLY SLOWS PROGRAM BY A LOT. Try looking at at at some point in the future
        #Check based on song names inside current directory and image names
        if not did_attribute:
            # TEMPPPPPPP
            audios_paths = Utils.get_audios_from_dir(audio_dir)
            for audio_path in audios_paths:
                index = 0
                while index < len(self.images_list):
                    audio_name = audio_path.stem
                    image_name = Utils.remove_extension(self.images_list[index])

                    if audio_name == image_name:
                        print(audio_name)
                        image_path = self.images_dir_path / self.images_list[index]
                        AudioFileTools.embed_image_safe(
                            audio_path,
                            image_path)
                        # Picture can't be attributed to another album
                        self.images_list.pop(index)
                        break
                    index += 1

        # recur in all child directories
        dirs_in_dir = Utils.get_dirs_from_dir(audio_dir)
        for dir in dirs_in_dir:
            self.embed_images_recursion_conditional(dir)


    # Currently not in use
    def embed_images_recursion(self, audio_dir: Path) -> None:
        """
        Recursively attributes images to songs.

        Function working order:
            If name of audio_dir is in images list, attribute image of this
            name to all audio files inside if at least one audio file inside
            does not have image embedded. If it's not, check if names of
            any audio files in audio_dir match names if images in image list and
            attribute accordingly. Recur in every directory inside audio_dir.

        Args:
            audio_dir (str): Path of a starting directory.
        Returns:
            None
        """
        matching_dir_name = Utils.strip_title(audio_dir.name)
        #lowercase for better name matching
        matching_dir_name_lowered = matching_dir_name.lower()
        index = 0
        did_attribute = False

        #Check based on directory name/image names
        while index < len(self.images_list):
            if matching_dir_name_lowered == Utils.remove_extension(self.images_list[index].lower()):
                print(matching_dir_name)
                image_path = self.images_dir_path / self.images_list[index]
                AudioDirTools.embed_img_file_to_audio_dir(
                    audio_dir,
                    image_path)
                # Picture can't be attributed to another album
                self.images_list.pop(index)
                did_attribute = True
                break
            index += 1

        #Check based on song names inside dir/image names
        if not did_attribute:
            # TEMPPPPPPP
            audios_paths = Utils.get_audios_from_dir(audio_dir)
            for audio_path in audios_paths:
                index = 0
                while index < len(self.images_list):
                    audio_name = audio_path.stem
                    image_name = Utils.remove_extension(self.images_list[index])

                    if audio_name == image_name:
                        print(audio_name)
                        image_path = self.images_dir_path / self.images_list[index]
                        AudioFileTools.embed_image_safe(
                            audio_path,
                            image_path)
                        # Picture can't be attributed to another album
                        self.images_list.pop(index)
                        break
                    index += 1

        dirs_in_dir = Utils.get_dirs_from_dir(audio_dir)
        for dir_path in dirs_in_dir:
            self.embed_images_recursion(dir_path)
