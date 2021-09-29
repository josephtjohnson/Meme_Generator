import os
import logging
from PIL import Image

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('imageresize.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def image_resize(self, img_path, width=500) -> str:
    """
    Resize an image to be used by make_meme()

    Paramters
    ---------
        img_path : str
            image file path
        width : int
            width of image in pixels (default = 500)
    """

    try:
        with Image.open(img_path) as img:
            ext = img_path.split('.')[-1]
            try:
                if width is not None and width <= 500:
                    ratio = width/float(img.size[0])
                    height = int(ratio*img.size[1])
                    img = img.resize((width, height))
                    return img
                else:
                    if width is None:
                        raise Exception('Width zero')
                    else:
                        raise Exception('Width >500')
            except Exception as e:
                logger.exception(f'Width must be <500 but greater than zero: {e}')
     except Exception as e:
        logger.exception(e)
        
