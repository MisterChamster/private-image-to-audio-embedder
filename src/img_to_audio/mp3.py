from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error



def has_image_mp3(file_path):
    try:
        audio = MP3(file_path, ID3=ID3)
        return any(tag.FrameID == "APIC" for tag in audio.tags.values())
    except Exception as e:
        print(f"Error reading MP3 file: {e}")
        print(r"Path of error file: ", file_path)
        return False


def embed_image_mp3(mp3_path, image_path):
    try:
        audio = ID3(mp3_path)
        with open(image_path, 'rb') as img:
            audio['APIC'] = APIC(
                encoding=3,         # 3 is for utf-8
                mime='image/jpeg',  # image type, you can use image/png or others
                type=3,             # 3 is for the cover (front) image
                desc=u'Cover',
                data=img.read())
        audio.save()
        # print(f"New image added to {file_path}")
    except error as e:
        print(f"Failed to add image: {e}")


def remove_image_mp3(mp3_path):
    try:
        audio = ID3(mp3_path)

        # Remove all APIC (attached picture) frames
        audio.delall("APIC")
        audio.save()
        # print(f"All embedded images removed from {file_path}")
    except error as e:
        print(f"Failed to remove images: {e}")
