from os import path, chdir, getcwd
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
            2. If it's not, check if names of any audio files in cwd
            match names of images in image list and attribute accordingly.
            3. Recur in every directory inside cwd.

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
            cwd_audio_path = audio_paths[index]
            is_embedded = AudioFileTools.is_image_embedded(cwd_audio_path)
            if not is_embedded:
                not_all_songs_embedded = True
                break
            index += 1

        #Check based on current directory name and image name
        did_attribute = False
        cwd_name = Utils.strip_title(audio_dir.stem)
        #lowercase for better name matching
        cwd_name_lowered = cwd_name.lower()

        ogpath = Path.cwd()
        chdir(audio_dir)

        if not_all_songs_embedded:
            index = 0
            while index < len(self.images_list):

                if cwd_name_lowered == Utils.remove_extension(self.images_list[index].lower()):
                    print(cwd_name)
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
            audios_in_cwd = Utils.get_audios_from_dir(Path.cwd())
            for audioname in audios_in_cwd:
                index = 0
                while index < len(self.images_list):
                    audio_file_no_ext = Utils.remove_extension(audioname)
                    image_file_no_ext = Utils.remove_extension(self.images_list[index])

                    if audio_file_no_ext == image_file_no_ext:
                        print(audio_file_no_ext)
                        audio_path = Path.cwd() / audioname
                        image_path = self.images_dir_path / self.images_list[index]
                        AudioFileTools.embed_image_safe(
                            audio_path,
                            image_path)
                        # Picture can't be attributed to another album
                        self.images_list.pop(index)
                        break
                    index += 1

        # recur in all child directories
        # TEMPPPPPPP
        dirs_in_dir = Utils.get_dirs_from_dir(Path.cwd())
        for dir in dirs_in_dir:
            self.embed_images_recursion_conditional(dir)

        chdir(ogpath)


    # Currently not in use
    def embed_images_recursion(self, audio_dir: Path) -> None:
        """
        Recursively attributes images to songs.

        Function working order:
            If name of audio_dir is in images list, attribute image of this
            name to all audio files inside if at least one audio file inside
            does not have image embedded. If it's not, check if names of
            any audio files in cwd match names if images in image list and
            attribute accordingly. Recur in every directory inside cwd.

        Args:
            audio_dir (str): Path of a starting directory.
        Returns:
            None
        """
        matching_CWDname = Utils.strip_title(audio_dir.name)
        #lowercase for better name matching
        matching_CWDname_lowered = matching_CWDname.lower()
        index = 0
        did_attribute = False

        ogpath = Path.cwd()
        chdir(audio_dir)

        #Check based on directory name/image names
        while index < len(self.images_list):
            if matching_CWDname_lowered == Utils.remove_extension(self.images_list[index].lower()):
                print(matching_CWDname)
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
            audios_in_cwd = Utils.get_audios_from_dir(Path.cwd())
            for audioname in audios_in_cwd:
                index = 0
                while index < len(self.images_list):
                    audio_file_no_ext = Utils.remove_extension(audioname)
                    image_file_no_ext = Utils.remove_extension(self.images_list[index])

                    if audio_file_no_ext == image_file_no_ext:
                        print(audio_file_no_ext)
                        audio_path = Path.cwd() / audioname
                        image_path = self.images_dir_path / self.images_list[index]
                        AudioFileTools.embed_image_safe(
                            audio_path,
                            image_path)
                        # Picture can't be attributed to another album
                        self.images_list.pop(index)
                        break
                    index += 1

        dirs_in_dir = Utils.get_dirs_from_dir(Path.cwd())
        for dir_path in dirs_in_dir:
            self.embed_images_recursion(dir_path)

        chdir(ogpath)
