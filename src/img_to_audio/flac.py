from mutagen.flac import FLAC, Picture



def embed_image_flac(flac_path, image_path):
    try:
        audio = FLAC(flac_path)
        image = Picture()
        with open(image_path, 'rb') as img:
            image.data = img.read()
        
        image.type = 3  # Cover (front)
        image.mime = "image/jpeg" if image_path.lower().endswith(".jpg") else "image/png"
        image.desc = "Cover"
        image.width = 0  # Optional: set image dimensions, if known
        image.height = 0
        image.depth = 0

        # Add the picture to the FLAC file
        audio.add_picture(image)
        audio.save()
    except Exception as e:
        print(f"Failed to add image: {e}")
