import os
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

            if width is not None and width <= 500:
                ratio = width/float(img.size[0])
                height = int(ratio*img.size[1])
                img = img.resize((width, height))
            else:
                if width is None:
                    raise Exception('Width cannot be zero')
                else:
                    raise Exception('Width cannot be >500')

            font = ImageFont.load_default()

            draw = ImageDraw.Draw(img)
            draw.text((10, 10), 'text', font=font)
            draw.text((10, 25), 'author', font=font)
            img.save(self.output)
            return self.output

        raise Exception('Unable to open image file. {img_path}')
