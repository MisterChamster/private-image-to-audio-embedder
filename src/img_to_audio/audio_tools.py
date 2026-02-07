from src.utils import Utils
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
from src.img_to_audio.mp3 import embed_image_mp3
from src.img_to_audio.flac import embed_image_flac



class AudioTools():
    @staticmethod
    def is_image_embedded(audio_path):
        if Utils.get_extension(audio_path) == "mp3":
            try:
                audio = MP3(audio_path, ID3=ID3)
                return any(tag.FrameID == "APIC" for tag in audio.tags.values())
            except Exception as e:
                print(f"Error reading MP3 file: {e}")
                print(r"Path of error file: ", audio_path)
                return False

        elif Utils.get_extension(audio_path) == "flac":
            try:
                audio = FLAC(audio_path)
                return bool(audio.pictures)
            except Exception as e:
                print(f"Error reading FLAC file: {e}")
                print(r"Path of error file: ", audio_path)
                return False


    @staticmethod
    def remove_image(audio_path):
        if audio_path.endswith(".mp3"):
            try:
                audio = ID3(audio_path)
                audio.delall("APIC")
                audio.save()
            except error as e:
                print(f"Failed to remove images: {e}")

        elif audio_path.endswith(".flac"):
            try:
                audio = FLAC(audio_path)
                audio.clear_pictures()
                audio.save()
            except Exception as e:
                print(f"Failed to remove images: {e}")


    @staticmethod
    def embed_image_safe(audio_path, image_path):
        if AudioTools.is_image_embedded(audio_path):
            AudioTools.remove_image(audio_path)

        if Utils.get_extension(audio_path) == "mp3":
            embed_image_mp3(audio_path, image_path)

        elif Utils.get_extension(audio_path) == "flac":
            embed_image_flac(audio_path, image_path)
