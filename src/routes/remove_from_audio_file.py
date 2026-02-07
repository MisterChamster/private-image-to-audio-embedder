from src.img_to_audio.audio_tools import AudioTools
from src.askers import Askers



def remove_from_audio_file():
    print("Choose audio file")
    input_audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    AudioTools.remove_image(input_audio_file_path)
    print("Image succesfully removed\n\n")
