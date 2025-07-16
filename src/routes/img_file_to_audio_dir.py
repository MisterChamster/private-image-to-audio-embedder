from os import path
from src.img_to_audio.multiple_audio import embed_img_file_to_audio_dir
from src.askers import ask_path_filedialog



def img_file_to_audio_dir():
    print("Choose image file")
    input_image_file_path = ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {input_image_file_path}\n")
    print("Choose audio directory")
    input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    embed_img_file_to_audio_dir(input_audio_dir_path, input_image_file_path)
    print("Image successfully embedded to: " + path.basename(input_audio_dir_path) + "\n\n")
