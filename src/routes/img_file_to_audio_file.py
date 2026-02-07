from os import path
from src.img_to_audio.audio_tools import AudioTools
from src.askers import Askers



def img_file_to_audio_file():
    print("Choose image file")
    input_image_file_path = Askers.ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {input_image_file_path}\n")
    print("Choose audio file")
    input_audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    AudioTools.embed_image_safe(input_audio_file_path, input_image_file_path)
    print(path.basename(input_audio_file_path))
