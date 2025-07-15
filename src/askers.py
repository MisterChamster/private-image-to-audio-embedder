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
