from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
import logging
import argparse
import random
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def generate_meme(path=None, body=None, author=None, category=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        try:
            if category == 'dog':
                images = "./_data/photos/dog/"
            else:
                images = "./_data/photos/book/"
        except ValueError:
            logger.error('Default photo files not found')
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        try:
            if category == 'dog':
                quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                               './_data/DogQuotes/DogQuotesDOCX.docx',
                               './_data/DogQuotes/DogQuotesPDF.pdf',
                               './_data/DogQuotes/DogQuotesCSV.csv']
            else:
                quote_files = ['./_data/BookQuotes/BookQuotesDOCX.docx']
        except ValueError:
            logger.error('Default quote files not found')

        quotes = []
        for f in quote_files:
            try:
                quotes.extend(Ingestor.parse(f))
            except Exception:
                logger.error('Default quote files not found')
        
        quote = random.choice(quotes)

    else:
        try:
            if author is None:
        except:
            logger.error('Author Required if Body is Used')
                
        quote = QuoteModel(body, author)

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
        logger.error('Unable to parse arguements')
