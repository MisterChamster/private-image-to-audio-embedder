from src.img_to_audio.audio_dir_tools import embed_img_dir_to_audio_dir
from src.askers import Askers



def img_dir_to_audio_dir():
    print("Choose image directory")
    input_image_dir_path = Askers.ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {input_image_dir_path}\n")
    print("Choose audio directory")
    input_audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    embed_img_dir_to_audio_dir(input_audio_dir_path, input_image_dir_path)
