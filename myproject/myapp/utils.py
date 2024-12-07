import hashlib
from PIL import Image



def calculate_md5(image_content):
    md5 = hashlib.md5()
    md5.update(image_content)
    return md5.hexdigest()

def calculate_phash(image):
    """Calculate the perceptual hash (pHash) of an image."""
    image = image.convert('L').resize((8, 8), Image.ANTIALIAS)
    pixels = list(image.getdata())
    avg_pixel = sum(pixels) / len(pixels)
    bits = ''.join('1' if pixel > avg_pixel else '0' for pixel in pixels)
    hex_representation = hex(int(bits, 2))[2:].rjust(16, '0')
    return hex_representation