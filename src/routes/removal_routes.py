from src.img_to_audio.audio_dir_tools import AudioDirTools
from src.img_to_audio.audio_file_tools import AudioFileTools
from src.askers import Askers



def remove_from_audio_file() -> None:
    print("Choose audio file")
    input_audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    AudioFileTools.remove_image(input_audio_file_path)
    print("Image succesfully removed\n\n")
    return


def remove_from_audio_dir() -> None:
    print("Choose audio directory")
    input_audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    AudioDirTools.remove_images_dir(input_audio_dir_path)
    print("Images succesfully removed\n\n")
    return


def remove_from_audio_dir_recur() -> None:
    print("Choose audio directory")
    input_audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    AudioDirTools.remove_images_recursion(input_audio_dir_path)
    print("Images succesfully removed\n\n")
    return
