from os import path, chdir, getcwd
from src.img_to_audio.audio_file_tools import AudioFileTools
from src.utils import Utils
from src.img_to_audio.audio_dir_tools import AudioDirTools



class RecurringEmbedders():
    def __init__(self, images_dir):
        self.images_dir = images_dir
        self.images_list = Utils.get_images_list(images_dir)


    def embed_images_recursion_conditional(self, audio_dir: str) -> None:
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
        OGpath = getcwd()
        chdir(audio_dir)

        # Check if all songs have embedded image
        index = 0
        not_all_songs_embedded = False
        cwd_audios = Utils.get_audios_from_cwd()
        while index < len(cwd_audios):
            if not AudioFileTools.is_image_embedded(cwd_audios[index]):
                not_all_songs_embedded = True
                break
            index += 1

        #Check based on current directory name and image name
        index = 0
        did_attribute = False
        cwd_name = Utils.get_stripped_title(path.basename(getcwd()))
        #lowercase for better name matching
        cwd_name_lowered = cwd_name.lower()
        if not_all_songs_embedded == True:
            while index < len(self.images_list):
                if cwd_name_lowered == Utils.remove_extension(self.images_list[index].lower()):
                    print(cwd_name)
                    AudioDirTools.embed_img_file_to_audio_dir(getcwd(), self.images_dir + "/" + self.images_list[index])
                    # Picture can't be attributed to another album
                    self.images_list.pop(index)
                    did_attribute = True
                    break
                index += 1

        #THIS PROBABLY SLOWS PROGRAM BY A LOT. Try looking at at at some point in the future
        #Check based on song names inside current directory and image names
        if not did_attribute:
            audios_in_cwd = Utils.get_audios_from_cwd()
            for audioname in audios_in_cwd:
                index = 0
                while index < len(self.images_list):
                    if Utils.remove_extension(audioname) == Utils.remove_extension(self.images_list[index]):
                        print(Utils.remove_extension(audioname))
                        AudioFileTools.embed_image_safe(getcwd() + "/" + audioname, self.images_dir + "/" + self.images_list[index])
                        self.images_list.pop(index)          ###### Picture can't be attributed to another album
                        break
                    index += 1

        # recur in all child directories
        dirs_in_cwd = Utils.get_dirs_from_cwd()
        for dir in dirs_in_cwd:
            self.embed_images_recursion_conditional(dir)

        chdir(OGpath)


    # Currently not in use
    def embed_images_recursion(self, audio_dir: str) -> None:
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
        OGpath = getcwd()
        chdir(audio_dir)
        matching_CWDname = Utils.get_stripped_title(path.basename(getcwd()))
        matching_CWDname_lowered = matching_CWDname.lower()     #lowercase for better name matching
        index = 0
        did_attribute = False

        #Check based on directory name/image names
        while index < len(self.images_list):
            if matching_CWDname_lowered == Utils.remove_extension(self.images_list[index].lower()):
                print(matching_CWDname)
                AudioDirTools.embed_img_file_to_audio_dir(getcwd(), self.images_dir + "/" + self.images_list[index])
                self.images_list.pop(index)          ###### Picture can't be attributed to another album
                did_attribute = True
                break
            index += 1

        #Check based on song names inside dir/image names
        if not did_attribute:
            audios_in_cwd = Utils.get_audios_from_cwd()
            for audioname in audios_in_cwd:
                index = 0
                while index < len(self.images_list):
                    if Utils.remove_extension(audioname) == Utils.remove_extension(self.images_list[index]):
                        print(Utils.remove_extension(audioname))
                        AudioFileTools.embed_image_safe(getcwd() + "/" + audioname, self.images_dir + "/" + self.images_list[index])
                        self.images_list.pop(index)          ###### Picture can't be attributed to another album
                        break
                    index += 1

        dirs_in_cwd = Utils.get_dirs_from_cwd()
        for direct in dirs_in_cwd:
            self.embed_images_recursion(direct)

        chdir(OGpath)
