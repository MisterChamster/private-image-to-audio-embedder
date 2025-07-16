from src.img_to_audio.multiple_audio import embed_img_dir_to_audio_file
from src.askers import ask_path_filedialog



def img_dir_to_audio_file():
    print("Choose image directory")
    input_image_dir_path = ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {input_image_dir_path}\n")
    print("Choose audio file")
    input_audio_file_path = ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    embed_img_dir_to_audio_file(input_audio_file_path, input_image_dir_path)
    print(input_audio_file_path)
