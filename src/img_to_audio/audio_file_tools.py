from src.utils import Utils
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error



class AudioFileTools():
    # ======================== UNIVERSAL METHODS ========================
    @staticmethod
    def is_image_embedded(audio_path: str) -> bool:
        if Utils.get_extension(audio_path) == "mp3":
            AudioFileTools.is_image_embedded_mp3(audio_path)

        elif Utils.get_extension(audio_path) == "flac":
            AudioFileTools.is_image_embedded_flac(audio_path)
        return


    @staticmethod
    def remove_image(audio_path: str) -> None:
        if Utils.get_extension(audio_path) == "mp3":
            AudioFileTools.remove_image_mp3(audio_path)

        elif Utils.get_extension(audio_path) == "flac":
            AudioFileTools.remove_image_flac(audio_path)
        return


    @staticmethod
    def embed_image(audio_path: str, image_path: str) -> None:
        if Utils.get_extension(audio_path) == "mp3":
            AudioFileTools.embed_image_mp3(audio_path, image_path)

        elif Utils.get_extension(audio_path) == "flac":
            AudioFileTools.embed_image_flac(audio_path, image_path)
        return


    @staticmethod
    def embed_image_safe(audio_path: str, image_path: str) -> None:
        if AudioFileTools.is_image_embedded(audio_path):
            AudioFileTools.remove_image(audio_path)

        AudioFileTools.embed_image(audio_path, image_path)
        return



    # =========================== MP3 METHODS ===========================
    @staticmethod
    def is_image_embedded_mp3(audio_path: str) -> bool:
        try:
            audio = MP3(audio_path, ID3=ID3)
            return any(tag.FrameID == "APIC" for tag in audio.tags.values())
        except Exception as e:
            print(f"Error reading MP3 file: {e}")
            print(r"Path of error file: ", audio_path)
            return False


    @staticmethod
    def embed_image_mp3(audio_path: str, image_path: str) -> None:
        image_ext = Utils.get_extension(image_path)
        mime = ('image/jpeg' if image_ext in ['jpg', 'jpeg'] else
                'image/png'  if image_ext == 'png' else
                None)

        try:
            audio = ID3(audio_path)
            with open(image_path, 'rb') as img:
                audio['APIC'] = APIC(
                    encoding=3,   # 3 is for utf-8
                    mime=mime,    # image type, image/png or image/jpeg
                    type=3,       # 3 is for the cover (front) image
                    desc=u'Cover',
                    data=img.read())
            audio.save()
        except error as e:
            print(f"Failed to add image: {e}")


    @staticmethod
    def remove_image_mp3(audio_path: str) -> None:
        try:
            audio = ID3(audio_path)
            audio.delall("APIC")
            audio.save()
        except error as e:
            print(f"Failed to remove images: {e}")


    # =========================== FLAC METHODS ===========================
    @staticmethod
    def is_image_embedded_flac(audio_path: str) -> bool:
        try:
            audio = FLAC(audio_path)
            return bool(audio.pictures)
        except Exception as e:
            print(f"Error reading FLAC file: {e}")
            print(r"Path of error file: ", audio_path)
            return False


    @staticmethod
    def embed_image_flac(audio_path: str, image_path: str) -> None:
        image_ext = Utils.get_extension(image_path)
        mime = ('image/jpeg' if image_ext in ['jpg', 'jpeg'] else
                'image/png'  if image_ext == 'png' else
                None)

        try:
            audio = FLAC(audio_path)
            image = Picture()
            with open(image_path, 'rb') as img:
                image.data = img.read()

            image.type = 3  # Cover (front)
            image.mime = mime
            image.desc = "Cover"
            image.width = 0  # Optional: set image dimensions, if known
            image.height = 0
            image.depth = 0

            # Add the picture to the FLAC file
            audio.add_picture(image)
            audio.save()
        except Exception as e:
            print(f"Failed to add image: {e}")


    @staticmethod
    def remove_image_flac(audio_path: str) -> None:
        try:
            audio = FLAC(audio_path)
            audio.clear_pictures()
            audio.save()
        except Exception as e:
            print(f"Failed to remove images: {e}")
