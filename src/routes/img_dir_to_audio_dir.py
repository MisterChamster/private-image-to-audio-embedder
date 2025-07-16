from src.img_to_audio.multiple_audio import embed_img_dir_to_audio_dir
from src.askers import ask_path_filedialog



def img_dir_to_audio_dir():
    print("Choose image directory")
    input_image_dir_path = ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {input_image_dir_path}\n")
    print("Choose audio directory")
    input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    embed_img_dir_to_audio_dir(input_audio_dir_path, input_image_dir_path)
