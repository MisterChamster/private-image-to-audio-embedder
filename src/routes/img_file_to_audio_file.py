from os import path
from src.img_to_audio.general_audio import embed_image
from src.askers import ask_path_filedialog



def img_file_to_audio_file():
    print("Choose image file")
    input_image_file_path = ask_path_filedialog("f", "Image file path")
    print(f"Path chosen: {input_image_file_path}\n")
    print("Choose audio file")
    input_audio_file_path = ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    embed_image(input_audio_file_path, input_image_file_path)
    print(path.basename(input_audio_file_path))
