from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
import utils
import logging
import argparse
import random
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def generate_meme(path=None, body=None, author=None, category=None):
    """
    Generates a meme given a path and a quote from default locations or user-specified CLI arguements.
        
    Parameters
    ----------
        path : str
            image file location
        body : str
            quote body
        author : str
            quote author
        category : str
            meme category
    """   
    
    img = None
    quote = None

    # process image files 
    if path is None:
        try:
            img = open_image(category)
        except FileNotFoundError:
            logger.error('Default image files not found')
    else:
        img = path
    
    # process quote files and create QuoteModel object
    if body is None:
        try:
            quote = open_quote(category)
        except FileNotFoundError:
            logger.error('Default quote files not found')    
    else:
        try:
            if author is None:
        except:
            logger.exception('Author Required if Body is Used')
                
        quote = QuoteModel(body, author)
    
    # create the meme
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    print('Meme generated! File location:')
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate a meme!')
    parser.add_argument('--path', type=str, required=False, default=None,
                        help='Insert path to image file')
    parser.add_argument('--body', type=str, required=False, default=None,
                        help='Insert quote text')
    parser.add_argument('--author', type=str, required=False, default=None,
                        help='Insert author name')
    parser.add_argument('--category', type=str, required=False, default='dog',
                        help='Insert category name: book, dog')
    try:
        args = parser.parse_args()
        print(generate_meme(args.path, args.body, args.author, args.category))
    except SystemExit:
        logger.exception('Unable to parse arguements')
