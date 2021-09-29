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
    def __init__(self, output):
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
        try:
            with Image.open(img_path) as img:
                ext = img_path.split('.')[-1]
                try:
                    if width is not None and width <= 500:
                        ratio = width/float(img.size[0])
                        height = int(ratio*img.size[1])
                        img = img.resize((width, height))
                    else:
                        if width is None:
                            raise Exception('Width zero')
                        else:
                            raise Exception('Width >500')
                except Exception as e:
                    logger.exception(f'Width must be <500 but greater than zero: {e}')

                font = ImageFont.truetype('fonts/Courgette-Regular.ttf', 25)
                fill = (0, 0, 0)
                draw = ImageDraw.Draw(img)
                draw.text((25, 20), text=text, fill=fill, font=font)
                draw.text((25, 50), text='-'+author, fill=fill, font=font)
                save_dir = f'{self.output}/{random.randint(0,10000)}.{ext}'
                img.save(save_dir)
                return save_dir

        except ValueError:
            logger.exception(f'{img_path} not supported')
