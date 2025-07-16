from os import path, chdir, getcwd
from src.img_to_audio.general_audio import (is_image_embedded,
                                            embed_image)
from src.utils import (remove_extension,
                       get_dirs_from_cwd,
                       get_audios_from_cwd,
                       get_stripped_title,
                       get_images_list)
from src.img_to_audio.multiple_audio import embed_to_all_audios



class Embed_Recursive_Conditional():
    def __init__(self, images_dir):
        self.images_dir = images_dir
        self.images_list = get_images_list(images_dir)


    def embed_images_recursion_conditional(self, audio_dir):
        """
        Recursively attributes images to songs.

        Function working order:
            1. If name of audio_dir is in images list, 
            attribute image of this name to all audio files inside.
            2. If it's not, check if names of any audio files in cwd 
            match names if images in image list and attribute accordingly.
            3. Recur in every directory inside cwd.

        Args:
            audio_dir (str): Path of audio directory.
            images_dir (str): Path of images directory.
        Returns:
            None
        """
        OGpath = getcwd()
        chdir(audio_dir)

        # Check if all songs have embedded image
        index = 0
        not_all_songs_embedded = False
        cwd_audios = get_audios_from_cwd()
        while index < len(cwd_audios):
            if not is_image_embedded(cwd_audios[index]):
                not_all_songs_embedded = True
                break
            index += 1

        #Check based on current directory name and image name
        index = 0
        did_attribute = False
        cwd_name = get_stripped_title(path.basename(getcwd()))
        #lowercase for better name matching
        cwd_name_lowered = cwd_name.lower()
        if not_all_songs_embedded == True:
            while index < len(self.images_list):
                if cwd_name_lowered == remove_extension(self.images_list[index].lower()):
                    print(cwd_name)
                    embed_to_all_audios(getcwd(), self.images_dir + "/" + self.images_list[index])
                    # Picture can't be attributed to another album
                    self.images_list.pop(index)
                    did_attribute = True
                    break
                index += 1

        #THIS PROBABLY SLOWS PROGRAM BY A LOT. Try looking at at at some point in the future
        #Check based on song names inside current directory and image names
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

        # recur in all child directories
        dirs_in_cwd = get_dirs_from_cwd()
        for dir in dirs_in_cwd:
            self.embed_images_recursion_conditional(dir)

        chdir(OGpath)
