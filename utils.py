from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
from PIL import Image
import argparse
import random
import os
import textwrap
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('utils.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def open_image(category):
    """
    Opens an image from a user-specified category.

    Parameters
    ----------
    category : str
    image category (dog or book, default=dog)
    """

    images = "./_data/photos/book/"

    if category == 'dog':
        images = "./_data/photos/dog/"

    imgs = []

    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
        return random.choice(imgs)


def open_image_app():
    """
    Returns images for building the meme.

    Parameters
    ----------
    category : str
    image category (dog or book, default=dog)
    """

    images = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
        return imgs


def open_quote(category):
    """
    Opens a quote from a user-specified category.

    Parameters
    ----------
    category : str
    image category (dog or book, default=dog)
    """

    quote_files = ['./_data/BookQuotes/BookQuotesDOCX.docx']

    if category == 'dog':
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
        return random.choice(quotes)


def open_quote_app():
    """
    Return quotes for building the meme.

    Parameters
    ----------
    category : str
    image category (dog or book, default=dog)
    """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []

    for f in quote_files:
        quotes.extend(Ingestor.parse(f))
        return quotes


def image_resize(img_path, width=500):
    """
    Resize an image to be used by make_meme()

    Paramters
    ---------
    img_path : str
    image file path
    width : int
    width of image in pixels (default = 500)
    """

    MAX_WIDTH: int = 500

    assert width is not None, 'Width is zero'
    assert width >= MAX_WIDTH, 'Width > 500'
    img_path = img_path
    with Image.open(img_path) as img:
        ratio = width/float(img.size[0])
        height = int(ratio*img.size[1])
        img = img.resize((width, height))
        return img


def text_draw(draw, text, author, fill, font, width, height):
    """
    Draw text in random location on image.
    Paramters
    ---------
    draw : image object
        image
    text : str
        quote text
    author : str
        quote text
    fill : tuple
        text fill
    font : font object
        text font
    width : int
        image width
    height : int
        image height
    """

    x_max = int(0.6*width)
    y_max = int(0.8*height)
    x = random.randint(15, x_max)
    y = random.randint(20, y_max)
    wrap_limit = (width - x)*0.08
    text = textwrap.fill(text, wrap_limit)

    if len(text+author) > (height-y)*0.5:
        draw.text((20, 20), text=text+'\n'+'-'+author, fill=fill, font=font)
    else:
        draw.text((x, y), text=text+'\n'+'-'+author, fill=fill, font=font)

    return draw
