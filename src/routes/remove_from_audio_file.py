from src.img_to_audio.audio_file_tools import AudioFileTools
from src.askers import Askers



def remove_from_audio_file():
    print("Choose audio file")
    input_audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    AudioFileTools.remove_image(input_audio_file_path)
    print("Image succesfully removed\n\n")
