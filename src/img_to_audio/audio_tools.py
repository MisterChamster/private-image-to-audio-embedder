from src.utils import Utils
from src.img_to_audio.mp3 import (has_image_mp3,
                                     embed_image_mp3,
                                     remove_image_mp3)
from src.img_to_audio.flac import (has_image_flac,
                                      embed_image_flac,
                                      remove_image_flac)



class AudioTools():
    @staticmethod
    def is_image_embedded(audio_path):
        if Utils.get_extension(audio_path) == "mp3":
            return has_image_mp3(audio_path)
        elif Utils.get_extension(audio_path) == "flac":
            return has_image_flac(audio_path)


    @staticmethod
    def embed_image(audio_path, image_path):
        if Utils.get_extension(audio_path) == "mp3":
            remove_image_mp3(audio_path)
            embed_image_mp3(audio_path, image_path)
        elif Utils.get_extension(audio_path) == "flac":
            remove_image_flac(audio_path)
            embed_image_flac(audio_path, image_path)


    @staticmethod
    def remove_image(audio_path):
        if audio_path.endswith(".mp3"):
            remove_image_mp3(audio_path)
        elif audio_path.endswith(".flac"):
            remove_image_flac(audio_path)
