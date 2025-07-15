from tkinter import filedialog
import os



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


def ask_save_path(message):
    original_path = os.getcwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)
    folder_selected = filedialog.askdirectory(title=message)
    os.chdir(original_path)
    return folder_selected
