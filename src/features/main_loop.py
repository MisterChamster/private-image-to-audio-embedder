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
from src.routes.img_file_to_audio_file import img_file_to_audio_file
from src.routes.img_file_to_audio_dir import img_file_to_audio_dir
from src.routes.img_dir_to_audio_file import img_dir_to_audio_file
from src.routes.img_dir_to_audio_dir import img_dir_to_audio_dir
from src.routes.img_dir_to_audio_dir_recur import img_dir_to_audio_dir_recur
from src.routes.remove_from_audio_file import remove_from_audio_file
from src.routes.remove_from_audio_dir import remove_from_audio_dir
from src.routes.remove_from_audio_dir_recur import remove_from_audio_dir_recur



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
            img_file_to_audio_file()

        elif action == "img_file_to_audio_dir":
            img_file_to_audio_dir()

        elif action == "img_dir_to_audio_file":
            img_dir_to_audio_file()

        elif action == "img_dir_to_audio_dir":
            img_dir_to_audio_dir()

        elif action == "img_dir_to_audio_dir_recur":
            img_dir_to_audio_dir_recur()

        elif action == "remove_from_audio_file":
            remove_from_audio_file()

        elif action == "remove_from_audio_dir":
            remove_from_audio_dir()

        elif action == "remove_from_audio_dir_recur":
            remove_from_audio_dir_recur()
