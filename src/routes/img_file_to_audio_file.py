from os import path
from src.img_to_audio.audio_file_tools import AudioFileTools
from src.askers import Askers



def img_file_to_audio_file() -> None:
    print("Choose image file")
    input_image_file_path = Askers.ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {input_image_file_path}\n")
    print("Choose audio file")
    input_audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    AudioFileTools.embed_image_safe(input_audio_file_path, input_image_file_path)
    print(path.basename(input_audio_file_path))
