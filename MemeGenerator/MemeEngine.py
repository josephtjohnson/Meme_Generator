import os
import random
import utils
from utils import image_resize, text_draw
from typing import List
from PIL import Image, ImageFont, ImageDraw


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
        Receives the image path, quote, and author and returns the file
        save location of the generated meme.
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
        if output is not None:
            if not os.path.exists(self.output):
                os.mkdir(self.output)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Constructs attributes for meme and returns file save location
        for meme image.

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
        img = image_resize(img_path, width)
        ext = img_path.split('.')[-1]
        font = ImageFont.truetype('fonts/Courgette-Regular.ttf', 25)
        fill = (0, 0, 0)

        draw = ImageDraw.Draw(img)

        add_text = text_draw(draw, text, author, fill, font)

        save_dir = f'{self.output}/{random.randint(0,10000)}.{ext}'
        img.save(save_dir)
        return save_dir
