from mutagen.flac import FLAC, Picture



def has_image_flac(file_path):
    """
    Check if a FLAC file has an embedded image.
    
    Args:
        file_path (str): Path to the FLAC file.
    
    Returns:
        bool: True if the FLAC file has an embedded image, False otherwise.
    """
    try:
        audio = FLAC(file_path)
        return bool(audio.pictures)
    except Exception as e:
        print(f"Error reading FLAC file: {e}")
        print(r"Path of error file: ", file_path)
        return False


def embed_image_flac(flac_path, image_path):
    """
    Adds an image to a flac file.

    Args:
        flac_path (str):    Path of a flac file.
        image_path (str):   Path of an image.
    Returns:
        None
    """
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
        # print(f"New image added to {flac_path}")
    except Exception as e:
        print(f"Failed to add image: {e}")


def remove_image_flac(flac_path):
    """
    Removes an image from a flac file.

    Args:
        flac_path (str): Path of a flac file.
    Returns:
        None
    """
    try:
        audio = FLAC(flac_path)
        
        # Remove all pictures from the FLAC file
        audio.clear_pictures()
        audio.save()
        # print(f"All embedded images removed from {flac_path}")
    except Exception as e:
        print(f"Failed to remove images: {e}")
