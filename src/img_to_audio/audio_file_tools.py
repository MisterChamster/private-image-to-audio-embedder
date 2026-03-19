from mutagen.flac import FLAC, Picture
from mutagen.mp3  import MP3
from mutagen.id3  import ID3, APIC, error
from pathlib import Path

from src.utils import Utils



class AudioFileTools():
    # ======================== UNIVERSAL METHODS ========================
    @staticmethod
    def is_image_embedded(audio_path: Path) -> bool:
        extension = audio_path.suffix

        if extension == "mp3":
            AudioFileTools.__is_image_embedded_mp3(audio_path)
        elif extension == "flac":
            AudioFileTools.__is_image_embedded_flac(audio_path)


    @staticmethod
    def remove_image(audio_path: Path) -> None:
        extension = audio_path.suffix

        if extension == "mp3":
            AudioFileTools.__remove_image_mp3(audio_path)
        elif extension == "flac":
            AudioFileTools.__remove_image_flac(audio_path)


    @staticmethod
    def embed_image(audio_path: Path, image_path: Path) -> None:
        audio_extension = audio_path.suffix

        if audio_extension == "mp3":
            AudioFileTools.__embed_image_mp3(audio_path, image_path)
        elif audio_extension == "flac":
            AudioFileTools.__embed_image_flac(audio_path, image_path)


    @staticmethod
    def embed_image_safe(audio_path: Path, image_path: Path) -> None:
        if AudioFileTools.is_image_embedded(audio_path):
            AudioFileTools.remove_image(audio_path)

        AudioFileTools.embed_image(audio_path, image_path)


    # =========================== MP3 METHODS ===========================
    @staticmethod
    def __is_image_embedded_mp3(audio_path: Path) -> bool:
        try:
            audio = MP3(audio_path, ID3=ID3)
            return any(tag.FrameID == "APIC" for tag in audio.tags.values())
        except Exception as e:
            print(f"Error reading MP3 file: {e}")
            print(f"Path of error file: {audio_path}")
            return False


    @staticmethod
    def __embed_image_mp3(audio_path: Path, image_path: Path) -> None:
        image_ext = image_path.suffix
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
    def __remove_image_mp3(audio_path: Path) -> None:
        try:
            audio = ID3(audio_path)
            audio.delall("APIC")
            audio.save()
        except error as e:
            print(f"Failed to remove images: {e}")


    # =========================== FLAC METHODS ===========================
    @staticmethod
    def __is_image_embedded_flac(audio_path: Path) -> bool:
        try:
            audio = FLAC(audio_path)
            return bool(audio.pictures)
        except Exception as e:
            print(f"Error reading FLAC file: {e}")
            print(f"Path of error file: {audio_path}")
            return False


    @staticmethod
    def __embed_image_flac(audio_path: Path, image_path: Path) -> None:
        image_ext = image_path.suffix
        mime = ('image/jpeg' if image_ext in ['jpg', 'jpeg'] else
                'image/png'  if image_ext == 'png' else
                None)

        try:
            audio = FLAC(audio_path)
            image = Picture()
            with open(image_path, 'rb') as img:
                image.data = img.read()

            image.type   = 3  # Cover (front)
            image.mime   = mime
            image.desc   = "Cover"
            image.width  = 0  # Optional: set image dimensions, if known
            image.height = 0
            image.depth  = 0

            # Add the picture to the FLAC file
            audio.add_picture(image)
            audio.save()
        except Exception as e:
            print(f"Failed to add image: {e}")


    @staticmethod
    def __remove_image_flac(audio_path: Path) -> None:
        try:
            audio = FLAC(audio_path)
            audio.clear_pictures()
            audio.save()
        except Exception as e:
            print(f"Failed to remove images: {e}")
