from src.utils import get_images_list
from os import path, chdir, getcwd
from src.file_operations.general import (remove_extension,
                                         get_dirs_from_cwd,
                                         get_audios_from_cwd)
from src.file_operations.audio import embed_image
from src.utils import (get_stripped_title,
                       get_images_list)
from src.features.big_routes import embed_to_all_audios



class Embed_Recursive():
    def __init__(self, audio_dir, images_dir):
        self.audio_dir = audio_dir
        self.images_dir = images_dir
        self.images_list = get_images_list(images_dir)


    def embed_images_recursion(self):
        """
        Recursively attributes images to songs.

        Function working order:
            If name of audio_dir is in images list, attribute image of this name to 
            all audio files inside if at least one audio file inside does not have image embedded.
            If it's not, check if names of any audio files in cwd match names if images in image 
            list and attribute accordingly.
            Recur in every directory inside cwd.

        Args:
            audio_dir (str): Path of a starting directory.
            images_dir (str): Path of images directory.
        Returns:
            None
        """
        OGpath = getcwd()
        chdir(self.audio_dir)
        matching_CWDname = get_stripped_title(path.basename(getcwd()))
        matching_CWDname_lowered = matching_CWDname.lower()     #lowercase for better name matching
        index = 0
        did_attribute = False

        #Check based on directory name/image names
        while index < len(self.images_list):
            if matching_CWDname_lowered == remove_extension(self.images_list[index].lower()):
                print(matching_CWDname)
                embed_to_all_audios(getcwd(), self.images_dir + "/" + self.images_list[index])
                self.images_list.pop(index)          ###### Picture can't be attributed to another album
                did_attribute = True
                break
            index += 1

        #Check based on song names inside dir/image names
        if not did_attribute:
            audios_in_cwd = get_audios_from_cwd()
            for audioname in audios_in_cwd:
                index = 0
                while index < len(self.images_list):
                    if remove_extension(audioname) == remove_extension(self.images_list[index]):
                        print(remove_extension(audioname))
                        embed_image(getcwd() + "/" + audioname, self.images_dir + "/" + self.images_list[index])
                        self.images_list.pop(index)          ###### Picture can't be attributed to another album
                        break
                    index += 1


        dirs_in_cwd = get_dirs_from_cwd()
        for direct in dirs_in_cwd:
            self.embed_images_recursion()

        chdir(OGpath)

