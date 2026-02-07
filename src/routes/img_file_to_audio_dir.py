from os import path
from src.img_to_audio.audio_dir_tools import AudioDirTools
from src.askers import Askers



def img_file_to_audio_dir():
    print("Choose image file")
    input_image_file_path = Askers.ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {input_image_file_path}\n")
    print("Choose audio directory")
    input_audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    AudioDirTools.embed_img_file_to_audio_dir(input_audio_dir_path, input_image_file_path)
    print("Image successfully embedded to: " + path.basename(input_audio_dir_path) + "\n\n")
