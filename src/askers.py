from tkinter import filedialog
from typing import Literal
import os



class Askers():
    @staticmethod
    def ask_initial() -> str | None:
        returns_dict = {
            "ftf": "img_file_to_audio_file",
            "ftd": "img_file_to_audio_dir",
            "dtf": "img_dir_to_audio_file",
            "dtd": "img_dir_to_audio_dir",
            "dtdr": "img_dir_to_audio_dir_recur",
            "rmf": "remove_from_audio_file",
            "rmd": "remove_from_audio_dir",
            "rmdr": "remove_from_audio_dir_recur"}

        while True:
            print("Choose action:\n"
                  "ftf  - Image file to audio file\n"
                  "ftd  - Image file to audio directory\n"
                  "dtf  - Image directory to audio file\n"
                  "dtd  - Image directory to audio directory\n"
                  "dtdr - Image directory to audio directory (recursive)\n"
                  "rmf  - Remove image from audio file\n"
                  "rmd  - Remove image from audio directory\n"
                  "rmdr - Remove image from audio directory (recursive)\n"
                  "exit - Exit program\n>> ", end="")
            asker = input().strip().lower()

            if asker == "exit":
                return None
            elif asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_path_filedialog(
        type: Literal["f", "d"],
        message: str
    ) -> str:
        original_path = os.getcwd()
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)

        sel_path = ""
        if type == "f":
            sel_path = filedialog.askopenfilename(title=message)
        elif type == "d":
            sel_path = filedialog.askdirectory(title=message)

        os.chdir(original_path)
        return sel_path
