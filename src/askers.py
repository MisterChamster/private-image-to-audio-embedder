from tkinter import filedialog
import os



def ask_initial():
    returns_dict = {"ftf": "img_file_to_audio_file",
                    "ftd": "img_file_to_audio_dir",
                    "dtf": "img_dir_to_audio_file",
                    "dtd": "img_dir_to_audio_dir_recur",
                    "rmf": "remove_from_audio_file",
                    "rmd": "remove_from_audio_dir_recur"}

    while True:
        print("Choose action:\n" \
            "ftf  - Image file to audio file\n" \
            "ftd  - Image file to audio directory\n" \
            "dtf  - Image directory to audio file\n" \
            "dtdr - Image directory to audio directory (recursive)\n" \
            "rmf  - Remove image from audio file\n" \
            "rmdr - Remove image from audio directory (recursive)\n" \
            "exit - Exit program\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker not in ["ftf", "ftd", "dtf", "dtdr", "rmf", "rmdr"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]


def ask_embed_or_remove():
    returns_dict = {"e": "embed",
                    "r": "remove"}

    while True:
        print("Choose images embedding or removal:\n" \
              "(input 'exit' to exit)\n" \
              "e - embedding\n" \
              "r - removal\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif asker not in ["e", "r"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]


def ask_path_filedialog(type, message):
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
