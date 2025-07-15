from os import path, chdir, listdir, getcwd
from src.file_operations.general import (has_img_extension,
                                         remove_extension,
                                         get_dirs_from_cwd,
                                         get_audios_from_cwd)
from src.file_operations.audio import (has_image_audio,
                                       embed_image,
                                       remove_image)
from src.utils import get_stripped_title
from src.features.big_routes import (embed_to_all_audios,
                                     img_dir_to_audio_file,
                                     remove_images_recursion)


images_list = []
images_list_no_ext = []



def EmbedImagesRecursion(audio_dir, images_dir):
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
    chdir(audio_dir)
    matching_CWDname = get_stripped_title(path.basename(getcwd()))
    matching_CWDname_lowered = matching_CWDname.lower()     #lowercase for better name matching
    index = 0
    did_attribute = False

    #Check based on directory name/image names
    while index < len(images_list):
        if matching_CWDname_lowered == images_list_no_ext[index].lower():
            print(matching_CWDname)
            embed_to_all_audios(getcwd(), images_dir + "/" + images_list[index])
            images_list.pop(index)          ###### Picture can't be attributed to another album
            images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
            did_attribute = True
            break
        index += 1

    #Check based on song names inside dir/image names
    if not did_attribute:
        audios_in_cwd = get_audios_from_cwd()
        for audioname in audios_in_cwd:
            index = 0
            while index < len(images_list):
                if remove_extension(audioname) == images_list_no_ext[index]:
                    print(remove_extension(audioname))
                    embed_image(getcwd() + "/" + audioname, images_dir + "/" + images_list[index])
                    images_list.pop(index)          ###### Picture can't be attributed to another album
                    images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
                    break
                index += 1


    dirs_in_cwd = get_dirs_from_cwd()
    for direct in dirs_in_cwd:
        EmbedImagesRecursion(direct, images_dir)

    chdir(OGpath)

def EmbedImagesRecursionCONDITIONAL(audio_dir, images_dir):
    """
    Recursively attributes images to songs.

    Function working order:
        If name of audio_dir is in images list, attribute image of this name to all audio files inside.
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
    chdir(audio_dir)
    matching_CWDname = get_stripped_title(path.basename(getcwd()))
    matching_CWDname_lowered = matching_CWDname.lower()     #lowercase for better name matching
    index = 0
    index2 = 0
    did_attribute = False
    not_all_songs_embedded = 0
    audio_list = get_audios_from_cwd()

    while index2 < len(audio_list):
        if not has_image_audio(audio_list[index2]):
            not_all_songs_embedded = 1
            break
        index2 += 1

    #Check based on directory/image name
    if not_all_songs_embedded == 1:
        while index < len(images_list):
            if matching_CWDname_lowered == images_list_no_ext[index].lower():
                print(matching_CWDname)
                embed_to_all_audios(getcwd(), images_dir + "/" + images_list[index])
                images_list.pop(index)          ###### Picture can't be attributed to another album
                images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
                did_attribute = True
                break
            index += 1

    #Check based on song names inside dir/image names
    if not did_attribute:
        audios_in_cwd = get_audios_from_cwd()
        for audioname in audios_in_cwd:
            index = 0
            while index < len(images_list):
                if remove_extension(audioname) == images_list_no_ext[index]:
                    print(remove_extension(audioname))
                    embed_image(getcwd() + "/" + audioname, images_dir + "/" + images_list[index])
                    images_list.pop(index)          ###### Picture can't be attributed to another album
                    images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
                    break
                index += 1

    
    dirs_in_cwd = get_dirs_from_cwd()
    for direct in dirs_in_cwd:
        EmbedImagesRecursionCONDITIONAL(direct, images_dir)

    chdir(OGpath)

# The recursive function doesn't change names of audiofiles in cwd and instead 
# has a function that changes is separately, because there would be a 
# significant time loss



input_audio_path = r"c:\Users\root\Desktop\album"
input_images_path = r"c:\Users\root\Desktop\cover"

try:
    input_audio_path
    input_images_path
except:
    pass
else:
    if path.isdir(input_audio_path):
        audio_path_isdir = True
    else:
        audio_path_isdir = False
    if path.isdir(input_images_path):
        images_path_isdir = True
    else:
        images_path_isdir = False


    if audio_path_isdir == False and images_path_isdir == False:
        embed_image(input_audio_path, input_images_path)
        print(path.basename(input_audio_path))

    elif audio_path_isdir == True and images_path_isdir == False:
        embed_to_all_audios(input_audio_path, input_images_path)
        print(path.basename(input_images_path))
        # with the same name, any depth
        # EmbedImagesRecursion(input_audio_path)

    else:
        chdir(input_images_path)
        images_list = [node for node in listdir() if has_img_extension(node)]
        images_list_no_ext = [remove_extension(image) for image in images_list]
        if audio_path_isdir == False and images_path_isdir == True:
            img_dir_to_audio_file(input_audio_path, input_images_path, images_list, images_list_no_ext)
            print(input_audio_path)
            # print(path.basename(input_audio_path))

        elif audio_path_isdir == True and images_path_isdir == True:
            # EmbedImagesRecursion(input_audio_path, input_images_path)
            EmbedImagesRecursionCONDITIONAL(input_audio_path, input_images_path)


try:
    del_path
except:
    pass
else:
    if del_path.endswith("mp3") or del_path.endswith("flac"):
        remove_image(del_path)
    elif path.isdir(del_path):
        remove_images_recursion(del_path)