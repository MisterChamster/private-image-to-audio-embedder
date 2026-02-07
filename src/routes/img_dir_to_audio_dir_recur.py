from src.img_to_audio.recurring_embedders import RecurringEmbedders
from src.askers import Askers



def img_dir_to_audio_dir_recur() -> None:
    print("Choose image directory")
    input_image_dir_path = Askers.ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {input_image_dir_path}\n")
    print("Choose audio directory")
    input_audio_dir_path = Askers.ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    # recurrer_cond = RecurringEmbedders(input_image_dir_path)
    # recurrer_cond.embed_images_recursion(input_audio_dir_path)
    recurrer_cond = RecurringEmbedders(input_image_dir_path)
    recurrer_cond.embed_images_recursion_conditional(input_audio_dir_path)
