from src.img_to_audio.recurring_embedders import RecurringEmbedders
from src.img_to_audio.audio_dir_tools import AudioDirTools
from src.img_to_audio.audio_file_tools import AudioFileTools
from src.askers import Askers
from os import path



def img_dir_to_audio_dir_recur() -> None:
    print("Choose image directory")
    image_dir_path = Askers.ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {image_dir_path}\n")

    print("Choose audio directory")
    audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {audio_dir_path}\n")

    # recurrer_cond = RecurringEmbedders(image_dir_path)
    # recurrer_cond.embed_images_recursion(audio_dir_path)
    recurrer_cond = RecurringEmbedders(image_dir_path)
    recurrer_cond.embed_images_recursion_conditional(audio_dir_path)
    return


def img_dir_to_audio_dir() -> None:
    print("Choose image directory")
    image_dir_path = Askers.ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {image_dir_path}\n")

    print("Choose audio directory")
    audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {audio_dir_path}\n")

    AudioDirTools.embed_img_dir_to_audio_dir(audio_dir_path, image_dir_path)
    return


def img_dir_to_audio_file() -> None:
    print("Choose image directory")
    image_dir_path = Askers.ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {image_dir_path}\n")

    print("Choose audio file")
    audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {audio_file_path}\n")

    AudioDirTools.embed_img_dir_to_audio_file(audio_file_path, image_dir_path)
    print(audio_file_path)
    return


def img_file_to_audio_dir() -> None:
    print("Choose image file")
    image_file_path = Askers.ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {image_file_path}\n")

    print("Choose audio directory")
    audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {audio_dir_path}\n")

    AudioDirTools.embed_img_file_to_audio_dir(audio_dir_path, image_file_path)
    print("Image successfully embedded to: " + path.basename(audio_dir_path) + "\n\n")
    return


def img_file_to_audio_file() -> None:
    print("Choose image file")
    image_file_path = Askers.ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {image_file_path}\n")

    print("Choose audio file")
    audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {audio_file_path}\n")

    AudioFileTools.embed_image_safe(audio_file_path, image_file_path)
    print(path.basename(audio_file_path))
    return
