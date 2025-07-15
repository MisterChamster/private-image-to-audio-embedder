from os import path, chdir
from src.file_operations.audio import (embed_image,
                                       remove_image)
from src.features.big_routes import (embed_to_all_audios,
                                     img_dir_to_audio_file,
                                     remove_images_recursion)
from src.recurring_classes.embed_recursive import Embed_Recursive
from src.recurring_classes.embed_recursive_conditional import Embed_Recursive_Conditional
from src.askers import ask_path_filedialog, ask_initial



def main_loop():
    while True:
        print("=============================================================")
        print("==================       Welcome to        ==================")
        print("================== Image to audio embedder ==================")
        print("=============================================================\n\n")

        action = ask_initial()
        if action == None:
            return
        print()

        if action == "img_file_to_audio_file":
            print("Choose image file")
            input_images_path = ask_path_filedialog("f", "Image file path")
            print("Choose audio file")
            input_audio_path = ask_path_filedialog("f", "Audio file path")

            embed_image(input_audio_path, input_images_path)
            print(path.basename(input_audio_path))

        elif action == "img_file_to_audio_dir":
            print("Choose image file")
            input_images_path = ask_path_filedialog("f", "Image file path")
            print("Choose audio directory")
            input_audio_path = ask_path_filedialog("d", "Audio directory path")

            embed_to_all_audios(input_audio_path, input_images_path)
            print(path.basename(input_images_path))

        elif action == "img_dir_to_audio_file":
            print("Choose image directory")
            input_images_path = ask_path_filedialog("d", "Image directory path")
            print("Choose audio file")
            input_audio_path = ask_path_filedialog("f", "Audio file path")

            img_dir_to_audio_file(input_audio_path, input_images_path)
            print(input_audio_path)

        elif action == "img_dir_to_audio_dir":
            print("Choose image directory")
            input_images_path = ask_path_filedialog("d", "Image path")
            print("Choose audio directory")
            input_audio_path = ask_path_filedialog("d", "Audio directory path")

            # recurrer_cond = Embed_Recursive(input_images_path)
            # recurrer_cond.embed_images_recursion(input_audio_path)
            recurrer_cond = Embed_Recursive_Conditional(input_images_path)
            recurrer_cond.embed_images_recursion_conditional(input_audio_path)

        elif action == "remove_from_audio_file":
            print("Choose audio file")
            input_audio_path = ask_path_filedialog("f", "Audio file path")

            remove_image(input_audio_path)

        elif action == "remove_from_audio_dir":
            print("Choose audio directory")
            input_audio_path = ask_path_filedialog("d", "Audio directory path")

            remove_images_recursion(input_audio_path)

        # input_audio_path = r"c:\Users\root\Desktop\album"
        # input_images_path = r"c:\Users\root\Desktop\cover"
