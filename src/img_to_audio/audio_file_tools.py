import base64
from mutagen.mp3  import MP3
from mutagen.id3  import ID3, APIC, error
from mutagen.flac import FLAC, Picture
from mutagen.oggvorbis import OggVorbis
from pathlib import Path



class AudioFileTools():
    # ======================== UNIVERSAL METHODS ========================
    @staticmethod
    def is_image_embedded(audio_path: Path) -> bool:
        extension = audio_path.suffix

        if extension == ".mp3":
            AudioFileTools.__is_image_embedded_mp3(audio_path)
        elif extension == ".flac":
            AudioFileTools.__is_image_embedded_flac(audio_path)
        elif extension == ".ogg":
            AudioFileTools.__is_image_embedded_ogg(audio_path)


    @staticmethod
    def remove_image(audio_path: Path) -> None:
        extension = audio_path.suffix

        if extension == ".mp3":
            AudioFileTools.__remove_image_mp3(audio_path)
        elif extension == ".flac":
            AudioFileTools.__remove_image_flac(audio_path)
        elif extension == ".ogg":
            AudioFileTools.__remove_image_ogg(audio_path)


    @staticmethod
    def embed_image(audio_path: Path, image_path: Path) -> None:
        audio_extension = audio_path.suffix

        if audio_extension == ".mp3":
            AudioFileTools.__embed_image_mp3(audio_path, image_path)
        elif audio_extension == ".flac":
            AudioFileTools.__embed_image_flac(audio_path, image_path)
        elif audio_extension == ".ogg":
            AudioFileTools.__embed_image_ogg(audio_path, image_path)


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
        except Exception as e:
            print(f"Error reading MP3 file: {e}")
            print(f"Path of file: {audio_path}")
            return False

        return any(tag.FrameID == "APIC" for tag in audio.tags.values())


    @staticmethod
    def __embed_image_mp3(audio_path: Path, image_path: Path) -> None:
        image_ext = image_path.suffix
        image_stem = image_path.stem
        mime = ('image/jpeg' if image_ext in ['.jpg', '.jpeg'] else
                'image/png'  if image_ext == '.png' else
                None)

        try:
            audio = ID3(audio_path)
        except error as e:
            print(f"Failed to load audio file\n{e}")
            return

        try:
            with open(image_path, 'rb') as img:
                loaded_img = img.read()
        except error as e:
            print(f"Failed to load image file\n{e}")
            return

        try:
            audio['APIC'] = APIC(
                encoding=3,   # 3 is for utf-8
                mime=mime,    # image type, image/png or image/jpeg
                type=3,       # 3 is for the cover (front) image
                desc=image_stem,
                data=loaded_img)
            audio.save()
        except error as e:
            print(f"Failed to embed image\n{e}")


    @staticmethod
    def __remove_image_mp3(audio_path: Path) -> None:
        try:
            audio = ID3(audio_path)
        except error as e:
            print(f"Failed to load audio file\n{e}")
            return

        try:
            audio.delall("APIC")
            audio.save()
        except error as e:
            print(f"Failed to remove image: {e}")


    # =========================== FLAC METHODS ===========================
    @staticmethod
    def __is_image_embedded_flac(audio_path: Path) -> bool:
        try:
            audio = FLAC(audio_path)
        except Exception as e:
            print(f"Error reading FLAC file: {e}")
            print(f"Path of file: {audio_path}")
            return False

        return bool(audio.pictures)


    @staticmethod
    def __embed_image_flac(audio_path: Path, image_path: Path) -> None:
        image_ext = image_path.suffix
        image_stem = image_path.stem
        mime = ('image/jpeg' if image_ext in ['.jpg', '.jpeg'] else
                'image/png'  if image_ext == '.png' else
                None)

        try:
            audio = FLAC(audio_path)
        except error as e:
            print(f"Failed to load audio file\n{e}")
            return

        image = Picture()
        try:
            with open(image_path, 'rb') as img:
                loaded_img = img.read()
        except error as e:
            print(f"Failed to load image file\n{e}")
            return

        image.data = loaded_img
        image.type = 3
        image.mime = mime
        image.desc = image_stem

        try:
            audio.add_picture(image)
            audio.save()
        except Exception as e:
            print(f"Failed to embed image\n{e}")


    @staticmethod
    def __remove_image_flac(audio_path: Path) -> None:
        try:
            audio = FLAC(audio_path)
        except error as e:
            print(f"Failed to load audio file\n{e}")
            return

        try:
            audio.clear_pictures()
            audio.save()
        except Exception as e:
            print(f"Failed to remove image: {e}")


    # =========================== OGG METHODS ===========================
    @staticmethod
    def __is_image_embedded_ogg(audio_path: Path) -> bool:
        try:
            audio = OggVorbis(audio_path)
        except Exception as e:
            print(f"Error reading OGG file: {e}")
            print(f"Path of file: {audio_path}")
            return False

        has_cover = "metadata_block_picture" in audio
        return has_cover


    @staticmethod
    def __embed_image_ogg(audio_path: Path, image_path: Path) -> None:
        image_ext = image_path.suffix
        image_stem = image_path.stem
        mime = ('image/jpeg' if image_ext in ['.jpg', '.jpeg'] else
                'image/png'  if image_ext == '.png' else
                None)

        try:
            audio = OggVorbis(audio_path)
        except error as e:
            print(f"Failed to load audio file\n{e}")
            return

        pic = Picture()
        pic.type = 3  # 3 = front cover
        pic.mime = mime
        pic.desc = image_stem

        try:
            with open(image_path, 'rb') as img:
                loaded_img = img.read()
        except error as e:
            print(f"Failed to load image file\n{e}")
            return

        pic.data = loaded_img
        # Encode and store
        encoded = base64.b64encode(pic.write()).decode("ascii")

        try:
            audio["metadata_block_picture"] = [encoded]
            audio.save()
        except Exception as e:
            print(f"Failed to embed image\n{e}")


    @staticmethod
    def __remove_image_ogg(audio_path: Path) -> None:
        try:
            audio = OggVorbis(audio_path)
        except error as e:
            print(f"Failed to load audio file\n{e}")
            return

        try:
            if "metadata_block_picture" in audio:
                del audio["metadata_block_picture"]
                audio.save()
        except Exception as e:
            print(f"Failed to remove image: {e}")
