from os import path
from src.img_to_audio.general_audio import (embed_image,
                                            remove_image)
from src.img_to_audio.multiple_audio import (embed_img_file_to_audio_dir,
                                             embed_img_dir_to_audio_file,
                                             remove_images_recursion,
                                             remove_images_dir,
                                             embed_img_dir_to_audio_dir)
from src.img_to_audio.recurring_classes.embed_recursive import Embed_Recursive
from src.img_to_audio.recurring_classes.embed_recursive_conditional import Embed_Recursive_Conditional
from src.askers import ask_path_filedialog, ask_initial



def img_file_to_audio_file():
    return
