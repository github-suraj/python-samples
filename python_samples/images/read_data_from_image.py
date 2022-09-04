'''
    Module File to read Image
'''

import os
import base64
from PIL import Image
from pytesseract import pytesseract

PATH_TO_TESSERACT = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

def get_text_from_image(image_path, path_to_tesseract=None):
    '''
        Function to read Text from Image
    '''
    if not path_to_tesseract:
        path_to_tesseract = PATH_TO_TESSERACT

    # Opening the image and storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract executable
    pytesseract.tesseract_cmd = path_to_tesseract

    # Fetching text from image object
    return pytesseract.image_to_string(img)


def get_base64_from_image(image_path):
    '''
        Function to get base 64 binary data for Image
    '''
    with open(image_path, 'rb') as img:
        b64_str = base64.b64encode(img.read())
    return b64_str


if __name__ == '__main__':
    ifile = os.path.join('sample_docs', 'images', 'image_with_text.png')
    text = get_text_from_image(ifile)
    print(text)
    binary = get_base64_from_image(ifile)
    print(binary)
