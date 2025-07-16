from src.img_to_audio.general_audio import remove_image
from src.askers import ask_path_filedialog



def remove_from_audio_file():
    print("Choose audio file")
    input_audio_file_path = ask_path_filedialog("f", "Audio file path")
    print(f"Path chosen: {input_audio_file_path}\n")

    remove_image(input_audio_file_path)
    print("Image succesfully removed\n\n")
