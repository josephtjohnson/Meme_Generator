from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
import logging
import argparse
import random
import os

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

        
        
