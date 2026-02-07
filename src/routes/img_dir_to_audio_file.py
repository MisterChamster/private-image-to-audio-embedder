from src.img_to_audio.audio_dir_tools import AudioDirTools
from src.askers import Askers



def img_dir_to_audio_file() -> None:
    print("Choose image directory")
    input_image_dir_path = Askers.ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {input_image_dir_path}\n")
    print("Choose audio file")
    input_audio_file_path = Askers.ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    AudioDirTools.embed_img_dir_to_audio_file(input_audio_file_path, input_image_dir_path)
    print(input_audio_file_path)
