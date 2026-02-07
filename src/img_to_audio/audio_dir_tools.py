from os import path, chdir, getcwd
from src.utils import Utils
from src.img_to_audio.audio_file_tools import AudioFileTools



class AudioDirTools():
    @staticmethod
    def embed_img_file_to_audio_dir(audio_dir: str, image_path: str) -> None:
        """
        Embeds an image to all mp3 and flac files inside a directory.

        Args:
            album_dir  (str): Path of a directory containing audio files.
            image_path (str): Path of an image to embed.
        Returns:
            None
        """
        og_path = getcwd()
        chdir(audio_dir)
        songs_in_cd = Utils.get_audios_from_cwd()
        chdir(og_path)
        for audiofile in songs_in_cd:
            AudioFileTools.embed_image_safe(audio_dir + "/" + audiofile, image_path)


    @staticmethod
    def embed_img_dir_to_audio_file(audio_path: str, images_dir: str) -> None:
        images_list = Utils.get_images_list(images_dir)

        index = 0
        print(audio_path)
        audiofile_name = path.basename(audio_path)
        audiofile_name_no_ext = Utils.remove_extension(audiofile_name)

        while index < len(images_list):
            if audiofile_name_no_ext == Utils.remove_extension(images_list[index]):
                print(audiofile_name)
                AudioFileTools.embed_image_safe(audio_path, images_dir + "/" + images_list[index])
                images_list.pop(index)          ###### Picture can't be embedded to another album
                break
            index += 1


    @staticmethod
    def embed_img_dir_to_audio_dir(audio_dir: str, images_dir: str) -> None:
        OGpath = getcwd()
        chdir(audio_dir)

        images_list = Utils.get_images_list(images_dir)
        index = 0
        cwd_name = Utils.get_stripped_title(path.basename(getcwd()))
        #lowercase for better name matching
        cwd_name_lowered = cwd_name.lower()

        while index < len(images_list):
            if cwd_name_lowered == Utils.remove_extension(images_list[index].lower()):
                print(cwd_name)
                AudioDirTools.embed_img_file_to_audio_dir(getcwd(), images_dir + "/" + images_list[index])
                break
            index += 1

        chdir(OGpath)


    @staticmethod
    def remove_images_dir(dir_path: str) -> None:
        og_path = getcwd()
        chdir(dir_path)
        audios_list = Utils.get_audios_from_cwd()

        for audio in audios_list:
            AudioFileTools.remove_image(getcwd() + "/" + audio)

        chdir(og_path)


    @staticmethod
    def remove_images_recursion(dir_path: str) -> None:
        """
        Removes images embedded to mp3 and flac files present in a directory and 
        all the directories inside.

        Args:
            dir_path (str): Path of a directory.
        Returns:
            None
        """
        og_path = getcwd()
        chdir(dir_path)
        audios_list = Utils.get_audios_from_cwd()

        for audio in audios_list:
            AudioFileTools.remove_image(getcwd() + "/" + audio)

        dirs_in_cwd = Utils.get_dirs_from_cwd()
        for direct in dirs_in_cwd:
            AudioDirTools.remove_images_recursion(direct)

        chdir(og_path)


    # The recursive function doesn't change names of audiofiles in cwd and instead 
    # has a function that changes is separately, because there would be a 
    # significant time loss
