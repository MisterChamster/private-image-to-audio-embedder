# from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC, Picture
from mutagen.id3 import ID3, APIC, error
from os import path, chdir, listdir, getcwd
from src.file_operations.general import (has_img_extension,
                                         get_extension,
                                         remove_extension)
from src.file_operations.mp3 import (has_image_mp3,
                                     embed_image_mp3,
                                     remove_image_mp3)
from src.file_operations.flac import (has_image_flac,
                                      embed_image_flac,
                                      remove_image_flac)


images_list = []
images_list_no_ext = []

audio_path = r"c:\Users\root\Desktop\album"
images_path = r"c:\Users\root\Desktop\cover"


def MatchImageTitles(album_title):
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

def HasImageAudio(audio_path):
    """
    Checks if audio file (mp3, flac) has image embeddec.

    Args:
        audio_path (str): Path of a audio file.

    Returns:
        bool: If audio file has image embeddec. False otherwise.
    """
    if get_extension(audio_path) == "mp3":
        return has_image_mp3(audio_path)
    elif get_extension(audio_path) == "flac":
        return has_image_flac(audio_path)

def RemoveAndAddImageToAudiofile(audio_path, image_path):
    """
    Removes, than adds an image to a mp3 or flac file.

    Args:
        audio_path (str): Path of a audio file.
        image_path (str): Path of an image.
    Returns:
        None
    """
    if get_extension(audio_path) == "mp3":
        remove_image_mp3(audio_path)
        embed_image_mp3(audio_path, image_path)
    elif get_extension(audio_path) == "flac":
        remove_image_flac(audio_path)
        embed_image_flac(audio_path, image_path)

def RemoveImageFromAudio(audio_path):
    """
    Removes an embedded image from mp3 or flac file.

    Args:
        audio_path (str): Path of the audio file.
    Returns:
        None
    """
    if audio_path.endswith(".mp3"):
        remove_image_mp3(audio_path)
    elif audio_path.endswith(".flac"):
        remove_image_flac(audio_path)

def DirHasDirsInside(dir_path):
    """
    Checks if there are any directories inside a directory.

    Args:
        dir_path (str): Path of a directory to be checked.

    Returns:
        bool
    """
    OGpath = getcwd()
    chdir(dir_path)
    nodelist = listdir()
    chdir(OGpath)
    for node in nodelist:
        if path.isdir(dir_path + "/" + node):
            return True
    return False

def GetAudiosFromCWD():
    """
    Returns a list of mp3 and flac files in current working directory.

    Returns:
        list (str): Names of mp3 and flac files in current working directory.
    """
    audios_in_cwd = []
    for node in listdir():
        if get_extension(node) == "mp3" or get_extension(node) == "flac":
            audios_in_cwd.append(node)
    return audios_in_cwd

def GetDirsFromCWD():
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

def AddImageToAudiofilesInDir(album_path, image_path):
    """
    Adds an image to all mp3 and flac files inside a directory.

    Args:
        album_path (str): Path of a directory containing audio files.
        image_path (str): Path of an image to embed.
    Returns:
        None
    """
    OGpath = getcwd()
    chdir(album_path)
    songs_in_cd = GetAudiosFromCWD()
    chdir(OGpath)
    for audiofile in songs_in_cd:
        RemoveAndAddImageToAudiofile(album_path + "/" + audiofile, image_path)

def ImagedirToAudiofile(audio_path, images_dir):
    """
    To audio file, embeds an image with matching title.

    Args:
        audio_path (str): Path of an audio file.
        images_dir (str): Path of images directory.
    Returns:
        None
    """
    index = 0
    print(audio_path)
    audiofile_name = path.basename(audio_path)
    audiofile_name_no_ext = remove_extension(audiofile_name)

    while index < len(images_list_no_ext):
        if audiofile_name_no_ext == images_list_no_ext[index]:
            print(audiofile_name)
            RemoveAndAddImageToAudiofile(audio_path, images_dir + "/" + images_list[index])
            images_list.pop(index)          ###### Picture can't be embedded to another album
            images_list_no_ext.pop(index)   ###### Picture can't be embedded to another album
            break
        index += 1

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
    matching_CWDname = MatchImageTitles(path.basename(getcwd()))
    matching_CWDname_lowered = matching_CWDname.lower()     #lowercase for better name matching
    index = 0
    did_attribute = False

    #Check based on directory name/image names
    while index < len(images_list):
        if matching_CWDname_lowered == images_list_no_ext[index].lower():
            print(matching_CWDname)
            AddImageToAudiofilesInDir(getcwd(), images_dir + "/" + images_list[index])
            images_list.pop(index)          ###### Picture can't be attributed to another album
            images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
            did_attribute = True
            break
        index += 1

    #Check based on song names inside dir/image names
    if not did_attribute:
        audios_in_cwd = GetAudiosFromCWD()
        for audioname in audios_in_cwd:
            index = 0
            while index < len(images_list):
                if remove_extension(audioname) == images_list_no_ext[index]:
                    print(remove_extension(audioname))
                    RemoveAndAddImageToAudiofile(getcwd() + "/" + audioname, images_dir + "/" + images_list[index])
                    images_list.pop(index)          ###### Picture can't be attributed to another album
                    images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
                    break
                index += 1


    dirs_in_cwd = GetDirsFromCWD()
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
    matching_CWDname = MatchImageTitles(path.basename(getcwd()))
    matching_CWDname_lowered = matching_CWDname.lower()     #lowercase for better name matching
    index = 0
    index2 = 0
    did_attribute = False
    not_all_songs_embedded = 0
    audio_list = GetAudiosFromCWD()

    while index2 < len(audio_list):
        if not HasImageAudio(audio_list[index2]):
            not_all_songs_embedded = 1
            break
        index2 += 1

    #Check based on directory/image name
    if not_all_songs_embedded == 1:
        while index < len(images_list):
            if matching_CWDname_lowered == images_list_no_ext[index].lower():
                print(matching_CWDname)
                AddImageToAudiofilesInDir(getcwd(), images_dir + "/" + images_list[index])
                images_list.pop(index)          ###### Picture can't be attributed to another album
                images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
                did_attribute = True
                break
            index += 1

    #Check based on song names inside dir/image names
    if not did_attribute:
        audios_in_cwd = GetAudiosFromCWD()
        for audioname in audios_in_cwd:
            index = 0
            while index < len(images_list):
                if remove_extension(audioname) == images_list_no_ext[index]:
                    print(remove_extension(audioname))
                    RemoveAndAddImageToAudiofile(getcwd() + "/" + audioname, images_dir + "/" + images_list[index])
                    images_list.pop(index)          ###### Picture can't be attributed to another album
                    images_list_no_ext.pop(index)   ###### Picture can't be attributed to another album
                    break
                index += 1

    
    dirs_in_cwd = GetDirsFromCWD()
    for direct in dirs_in_cwd:
        EmbedImagesRecursionCONDITIONAL(direct, images_dir)

    chdir(OGpath)

def RemoveImagesRecursion(dir_path):
    """
    Removes images embedded to mp3 and flac files present in a directory and 
    all the directories inside.

    Args:
        dir_path (str): Path of a directory.
    Returns:
        None
    """
    OGpath = getcwd()
    chdir(dir_path)
    audios_list = GetAudiosFromCWD()

    for audio in audios_list:
        RemoveImageFromAudio(getcwd() + "/" + audio)

    dirs_in_cwd = GetDirsFromCWD()
    for direct in dirs_in_cwd:
        RemoveImagesRecursion(direct)

    chdir(OGpath)

# The recursive function doesn't change names of audiofiles in cwd and instead 
# has a function that changes is separately, because there would be a 
# significant time loss



try:
    audio_path
    images_path
except:
    pass
else:
    if path.isdir(audio_path):
        audio_path_isdir = True
    else:
        audio_path_isdir = False
    if path.isdir(images_path):
        chdir(images_path)
        images_list = [node for node in listdir() if has_img_extension(node)]
        images_list_no_ext = [remove_extension(image) for image in images_list]
        images_path_isdir = True
    else:
        images_path_isdir = False


    if audio_path_isdir == False and images_path_isdir == False:
        RemoveAndAddImageToAudiofile(audio_path, images_path)
        print(path.basename(audio_path))

    elif audio_path_isdir == True and images_path_isdir == False:
        AddImageToAudiofilesInDir(audio_path, images_path)
        print(path.basename(images_path))
        # with the same name, any depth
        # EmbedImagesRecursion(audio_path)

    else:
        if audio_path_isdir == False and images_path_isdir == True:
            ImagedirToAudiofile(audio_path, images_path)
            print(audio_path)
            # print(path.basename(audio_path))

        elif audio_path_isdir == True and images_path_isdir == True:
            # EmbedImagesRecursion(audio_path, images_path)
            EmbedImagesRecursionCONDITIONAL(audio_path, images_path)


try:
    del_path
except:
    pass
else:
    if del_path.endswith("mp3"):
        remove_image_mp3(del_path)
    elif del_path.endswith("flac"):
        remove_image_flac(del_path)
    elif path.isdir(del_path):
        RemoveImagesRecursion(del_path)