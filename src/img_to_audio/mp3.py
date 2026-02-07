from mutagen.id3 import ID3, APIC, error



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
    except error as e:
        print(f"Failed to add image: {e}")
