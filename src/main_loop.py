from src.askers import Askers
from src.routes.img_file_to_audio_file import img_file_to_audio_file
from src.routes.img_file_to_audio_dir import img_file_to_audio_dir
from src.routes.img_dir_to_audio_file import img_dir_to_audio_file
from src.routes.img_dir_to_audio_dir import img_dir_to_audio_dir
from src.routes.img_dir_to_audio_dir_recur import img_dir_to_audio_dir_recur
import src.routes.removal_routes as rmroutes



def main_loop() -> None:
    while True:
        print("=============================================================")
        print("==================       Welcome to        ==================")
        print("================== Image to audio embedder ==================")
        print("=============================================================\n\n")

        action = Askers.ask_initial()
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
            rmroutes.remove_from_audio_file()

        elif action == "remove_from_audio_dir":
            rmroutes.remove_from_audio_dir()

        elif action == "remove_from_audio_dir_recur":
            rmroutes.remove_from_audio_dir_recur()
