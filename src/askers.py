from tkinter import filedialog
from typing  import Literal
from pathlib import Path
import os



class Askers():
    project_path: Path


    @staticmethod
    def ask_initial() -> str | None:
        returns_dict = {
            "ff":  "img_file_to_audio_file",
            "fd":  "img_file_to_audio_dir",
            "df":  "img_dir_to_audio_file",
            "dd":  "img_dir_to_audio_dir",
            "ddr": "img_dir_to_audio_dir_recur",
            "rf":  "remove_from_audio_file",
            "rd":  "remove_from_audio_dir",
            "rdr": "remove_from_audio_dir_recur",
            "e":   "exit"}

        while True:
            print("Choose action:\n"
                  "ff  - Image file to audio file\n"
                  "fd  - Image file to audio directory\n"
                  "df  - Image directory to audio file\n"
                  "dd  - Image directory to audio directory\n"
                  "ddr - Image directory to audio directory (recursive)\n"
                  "rf  - Remove image from audio file\n"
                  "rd  - Remove image from audio directory\n"
                  "rdr - Remove image from audio directory (recursive)\n"
                  "e   - Exit program\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_path_filedialog(
        node_type: Literal["file", "dir"],
        file_type: Literal["audio", "image"]
    ) -> Path | None:
        original_path = Path.cwd()
        os.chdir(Askers.project_path)

        sel_path = ""
        if node_type == "file":
            if file_type == "image":
                message  = "Image file path"
                sel_path = filedialog.askopenfilename(
                    title=message,
                    filetypes=[("Image files",
                                "*.jpg *.jpeg *.png")])
            else:
                message  = "Audio file path"
                sel_path = filedialog.askopenfilename(
                    title=message,
                    filetypes=[("Audio files", "*.mp3 *.flac")])

        elif node_type == "dir":
            message = ("Image directory path"
                       if file_type == "image" else
                       "Audio directory path")
            sel_path = filedialog.askdirectory(title=message)

        os.chdir(original_path)
        if sel_path == "":
            return

        sel_path = Path(sel_path)
        return sel_path
