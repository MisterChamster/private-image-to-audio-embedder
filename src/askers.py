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
