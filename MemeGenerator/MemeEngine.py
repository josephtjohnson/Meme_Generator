import os
import random
from typing import List
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    def __init__(self, output):
        self.output = output
        if output is not None:
            if not os.path.exists(self.output):
                os.mkdir(self.output)
        else:
            raise Exception('Must provide file save location.')

    def make_meme(self, img_path, text, author, width=500) -> str:
        with Image.open(img_path) as img:
            ext = img_path.split('.')[-1]
            if width is not None and width <= 500:
                ratio = width/float(img.size[0])
                height = int(ratio*img.size[1])
                img = img.resize((width, height))
            else:
                if width is None:
                    raise Exception('Width cannot be zero')
                else:
                    raise Exception('Width cannot be >500')

            font = ImageFont.truetype('fonts/Courgette-Regular.ttf', 25)
            fill = (0, 0, 0)
            draw = ImageDraw.Draw(img)
            draw.text((25, 20), text=text, fill=fill, font=font)
            draw.text((25, 50), text='-'+author, fill=fill, font=font)
            save_dir = f'{self.output}/{random.randint(0,10000)}.{ext}'
            img.save(save_dir)
            return save_dir

        raise Exception('Unable to open image file. {img_path}')
