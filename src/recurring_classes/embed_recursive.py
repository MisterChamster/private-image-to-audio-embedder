from src.utils import get_images_list



class Embed_Recursive():
    def __init__(self, audio_dir, images_dir):
        self.audio_dir = audio_dir
        self.images_list = get_images_list(images_dir)
