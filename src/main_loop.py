from src.askers import Askers
import src.routes.removal_routes as rmroutes
import src.routes.embedding_routes as embroutes



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
            embroutes.img_file_to_audio_file()

        elif action == "img_file_to_audio_dir":
            embroutes.img_file_to_audio_dir()

        elif action == "img_dir_to_audio_file":
            embroutes.img_dir_to_audio_file()

        elif action == "img_dir_to_audio_dir":
            embroutes.img_dir_to_audio_dir()

        elif action == "img_dir_to_audio_dir_recur":
            embroutes.img_dir_to_audio_dir_recur()

        elif action == "remove_from_audio_file":
            rmroutes.remove_from_audio_file()

        elif action == "remove_from_audio_dir":
            rmroutes.remove_from_audio_dir()

        elif action == "remove_from_audio_dir_recur":
            rmroutes.remove_from_audio_dir_recur()
