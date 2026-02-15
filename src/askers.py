from tkinter import filedialog
from typing import Literal
from pathlib import Path
import os



class Askers():
    project_path: Path


    @staticmethod
    def ask_initial() -> str | None:
        returns_dict = {
            "ftf":  "img_file_to_audio_file",
            "ftd":  "img_file_to_audio_dir",
            "dtf":  "img_dir_to_audio_file",
            "dtd":  "img_dir_to_audio_dir",
            "dtdr": "img_dir_to_audio_dir_recur",
            "rmf":  "remove_from_audio_file",
            "rmd":  "remove_from_audio_dir",
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
        node_type: Literal["file", "dir"],
        file_type: Literal["audio", "image"]
    ) -> str:
        original_path = os.getcwd()
        os.chdir(Askers.project_path)

        sel_path = ""
        if node_type == "file":
            if file_type == "image":
                message = "Image file path"
                sel_path = filedialog.askopenfilename(
                    title=message,
                    filetypes=[
                        ("Image files", "*.jpg *.jpeg *.png")])
            else:
                message = "Audio file path"
                sel_path = filedialog.askopenfilename(
                    title=message,
                    filetypes=[
                        ("Audio files", "*.mp3 *.flac")])

        elif node_type == "dir":
            message = (
                "Image directory path"
                if file_type == "image" else
                "Audio directory path")
            sel_path = filedialog.askdirectory(title=message)

        os.chdir(original_path)
        return sel_path
