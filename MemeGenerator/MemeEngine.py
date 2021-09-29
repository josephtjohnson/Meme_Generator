import os
import random
import logging
from typing import List
from PIL import Image, ImageFont, ImageDraw

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('memegenerator.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class MemeEngine:
    """
    A class to represent a meme.
    ...
    Attributes
    ----------
    output : str
        file save location
    img_path : str
        image file path
    text : str
        quote text
    author : str
        quote author
    width : int
        width of image in pixels (default = 500)
        
    Methods
    -------
    make_meme(img_path, text, author, width=500):
        Receives the image path, quote, and author and returns the file save location of the generated meme.
    """
    
    def __init__(self, output):
        """
        Constructs attribute for save location object.
        
        Parameters
        ----------
            output : str
                file save location
        """                
        
        self.output = output
        try:
            if output is not None:
                try:
                    if not os.path.exists(self.output):
                        os.mkdir(self.output)
                except Exception:
                    logger.exception('Could not create output directory')
         except ValueError:
            logger.exception('File save location cannot be None')

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Constructs attributes for meme and returns file save location for meme image.
        
        Parameters
        ----------
            img_path : str
                image file path
            text : str
                quote text
            author : str
                quote author
            width : int
                width of image in pixels (default = 500)
        """
        img_path = img_path
        text = text
        author = author
        width = width
        
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
              
            try:
                img = image_resize(img_path, width)

                font = ImageFont.truetype('fonts/Courgette-Regular.ttf', 25)
                fill = (0, 0, 0)
                draw = ImageDraw.Draw(img)
                draw.text((25, 20), text=text, fill=fill, font=font)
                draw.text((25, 50), text='-'+author, fill=fill, font=font)
                save_dir = f'{self.output}/{random.randint(0,10000)}.{ext}'
                img.save(save_dir)
                return save_dir

            except Exception as e:
            logger.exception(f'Image unable to be resized : {e}')
