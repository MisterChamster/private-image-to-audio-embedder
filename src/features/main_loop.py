from os import path
from src.img_to_audio.general_audio import (embed_image,
                                            remove_image)
from src.img_to_audio.multiple_audio import (embed_img_file_to_audio_dir,
                                             embed_img_dir_to_audio_file,
                                             remove_images_recursion,
                                             remove_images_dir,
                                             embed_img_dir_to_audio_dir)
from src.img_to_audio.recurring_classes.embed_recursive import Embed_Recursive
from src.img_to_audio.recurring_classes.embed_recursive_conditional import Embed_Recursive_Conditional
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
            input_image_file_path = ask_path_filedialog("f", "Image file path")
            print(f"Path chosen: {input_image_file_path}\n")
            print("Choose audio file")
            input_audio_file_path = ask_path_filedialog("f", "Audio file path")
            print(f"Path chosen: {input_audio_file_path}\n")

            embed_image(input_audio_file_path, input_image_file_path)
            print(path.basename(input_audio_file_path))

        elif action == "img_file_to_audio_dir":
            print("Choose image file")
            input_image_file_path = ask_path_filedialog("f", "Image file path")
            print(f"Path chosen: {input_image_file_path}\n")
            print("Choose audio directory")
            input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
            print(f"Path chosen: {input_audio_dir_path}\n")

            embed_img_file_to_audio_dir(input_audio_dir_path, input_image_file_path)
            print("Image successfully embedded to: " + path.basename(input_audio_dir_path) + "\n\n")

        elif action == "img_dir_to_audio_file":
            print("Choose image directory")
            input_image_dir_path = ask_path_filedialog("d", "Image directory path")
            print(f"Path chosen: {input_image_dir_path}\n")
            print("Choose audio file")
            input_audio_file_path = ask_path_filedialog("f", "Audio file path")
            print(f"Path chosen: {input_audio_file_path}\n")

            embed_img_dir_to_audio_file(input_audio_file_path, input_image_dir_path)
            print(input_audio_file_path)

        elif action == "img_dir_to_audio_dir":
            print("Choose image directory")
            input_image_dir_path = ask_path_filedialog("d", "Image directory path")
            print(f"Path chosen: {input_image_dir_path}\n")
            print("Choose audio directory")
            input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
            print(f"Path chosen: {input_audio_dir_path}\n")

            embed_img_dir_to_audio_dir(input_audio_dir_path, input_image_dir_path)

        elif action == "img_dir_to_audio_dir_recur":
            print("Choose image directory")
            input_image_dir_path = ask_path_filedialog("d", "Image directory path")
            print(f"Path chosen: {input_image_dir_path}\n")
            print("Choose audio directory")
            input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
            print(f"Path chosen: {input_audio_dir_path}\n")

            # recurrer_cond = Embed_Recursive(input_image_dir_path)
            # recurrer_cond.embed_images_recursion(input_audio_dir_path)
            recurrer_cond = Embed_Recursive_Conditional(input_image_dir_path)
            recurrer_cond.embed_images_recursion_conditional(input_audio_dir_path)

        elif action == "remove_from_audio_file":
            print("Choose audio file")
            input_audio_file_path = ask_path_filedialog("f", "Audio file path")
            print(f"Path chosen: {input_audio_file_path}\n")

            remove_image(input_audio_file_path)
            print("Image succesfully removed\n\n")

        elif action == "remove_from_audio_dir":
            print("Choose audio directory")
            input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
            print(f"Path chosen: {input_audio_dir_path}\n")

            remove_images_dir(input_audio_dir_path)
            print("Images succesfully removed\n\n")

        elif action == "remove_from_audio_dir_recur":
            print("Choose audio directory")
            input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
            print(f"Path chosen: {input_audio_dir_path}\n")

            remove_images_recursion(input_audio_dir_path)
            print("Images succesfully removed\n\n")

        # input_audio_path = r"c:\Users\root\Desktop\album"
        # input_images_path = r"c:\Users\root\Desktop\cover"
