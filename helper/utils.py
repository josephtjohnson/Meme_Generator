from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
from PIL import Image
import logging
import argparse
import random
import os
impor textwrap

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('utils.log')
file_handler.setLevel(logging.ERROR)
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
  try:
    if category == 'dog':
        images = "./_data/photos/dog/"
    else:
        images = "./_data/photos/book/"
  except ValueError:
    logger.exception('Default photo files not found')
  try:
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files] 
    return random.choice(imgs)
  except Exception:
    logger.exception('Could not open image file')

  def open_quote(category):
  """
  Opens an image from a user-specified category.
  
  Parameters
  ----------
    category : str
      image category (dog or book, default=dog)
  """
  
  try:
    if category == 'dog':
      quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                     './_data/DogQuotes/DogQuotesDOCX.docx',
                     './_data/DogQuotes/DogQuotesPDF.pdf',
                     './_data/DogQuotes/DogQuotesCSV.csv']
    else:
        quote_files = ['./_data/BookQuotes/BookQuotesDOCX.docx']
  except ValueError:
      logger.exception('Default quote files not found')
  try:
    quotes = []
    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
            return random.choice(quotes)
        except Exception:
            logger.exception('Unable to parse quote files')
  except Exception as e:
    logger.exception(e)

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
        
def text_draw(draw, text, author, fill, font):
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
    """ 
    
    try:
      draw = draw
      x = random.randint(15,55)
      y = random.randint(20,70)
    except Exception:
      logger.exception('Could not open image')
    try:
      text = textwrap.fill(text, 30)
    except Exception:
      logger.exception('Could not wrap text')
    draw.text((x, y), text=text, fill=fill, font=font)
    draw.text((x, y+20), text='-'+author, fill=fill, font=font)
    return draw
