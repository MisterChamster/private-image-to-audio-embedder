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

        elif action == "img_file_to_audio_dir":
            print("Choose image file")
            input_images_path = ask_path_filedialog("f", "Image file path")
            print("Choose audio directory")
            input_audio_path = ask_path_filedialog("d", "Audio directory path")

        elif action == "img_dir_to_audio_file":
            print("Choose image directory")
            input_images_path = ask_path_filedialog("d", "Image directory path")
            print("Choose audio file")
            input_audio_path = ask_path_filedialog("f", "Audio file path")

        elif action == "img_dir_to_audio_dir":
            print("Choose image directory")
            input_images_path = ask_path_filedialog("d", "Image path")
            print("Choose audio directory")
            input_audio_path = ask_path_filedialog("d", "Audio directory path")

        elif action == "remove_from_audio_file":
            print("Choose audio file")
            input_audio_path = ask_path_filedialog("f", "Audio file path")

        elif action == "remove_from_audio_dir":
            print("Choose audio directory")
            input_audio_path = ask_path_filedialog("d", "Audio directory path")



        # input_audio_path = r"c:\Users\root\Desktop\album"
        # input_images_path = r"c:\Users\root\Desktop\cover"

        try:
            input_audio_path
            input_images_path
        except:
            pass
        else:
            if path.isdir(input_audio_path):
                audio_path_isdir = True
            else:
                audio_path_isdir = False
            if path.isdir(input_images_path):
                images_path_isdir = True
            else:
                images_path_isdir = False


            if audio_path_isdir == False and images_path_isdir == False:
                embed_image(input_audio_path, input_images_path)
                print(path.basename(input_audio_path))

            elif audio_path_isdir == True and images_path_isdir == False:
                embed_to_all_audios(input_audio_path, input_images_path)
                print(path.basename(input_images_path))

            else:
                chdir(input_images_path)
                if audio_path_isdir == False and images_path_isdir == True:
                    img_dir_to_audio_file(input_audio_path, input_images_path)
                    print(input_audio_path)
                    # print(path.basename(input_audio_path))

                elif audio_path_isdir == True and images_path_isdir == True:
                    # recurrer_cond = Embed_Recursive(input_images_path)
                    # recurrer_cond.embed_images_recursion(input_audio_path)

                    recurrer_cond = Embed_Recursive_Conditional(input_images_path)
                    recurrer_cond.embed_images_recursion_conditional(input_audio_path)


        try:
            del_path
        except:
            pass
        else:
            if del_path.endswith("mp3") or del_path.endswith("flac"):
                remove_image(del_path)
            elif path.isdir(del_path):
                remove_images_recursion(del_path)
