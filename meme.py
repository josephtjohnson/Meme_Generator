from Ingestors import Ingestor
from QuoteEngine import MemeEngine, QuoteModel
import argparse
import random
import os


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None
    try:
        if path is None:
            images = "./_data/photos/dog/"
            imgs = []
            for root, dirs, files in os.walk(images):
                imgs = [os.path.join(root, name) for name in files]
        else:
            img = path[0]           
    except FileNotFoundError:
        print(f'Default image file location -- {images} -- not found.')
    else:
        img = random.choice(imgs)
    finally:
        print('image finally statement executed')

    try:    
        if body is None:
            quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                           './_data/DogQuotes/DogQuotesDOCX.docx',
                           './_data/DogQuotes/DogQuotesPDF.pdf',
                           './_data/DogQuotes/DogQuotesCSV.csv']
            quotes = []
            for f in quote_files:
                quotes.extend(Ingestor.parse(f))

            quote = random.choice(quotes)
        else:
            if author is None:
                raise Exception('Author Required if Body is Used')
            
    except FileNotFoundError:
        print(f'Default quote file location -- {quote_files} -- not found.')
    else:
        quote = QuoteModel(body, author)
        meme = MemeGenerator('./tmp')
        path = meme.make_meme(img, quote.body, quote.author)
        return path
    finally:
        print(' body/author finally statement executed')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a meme!')
    parser.add_argument('--path', type=str, required=False, default=None, help='Insert path to image file')
    parser.add_argument('--body', type=str, required=False, default=None, help='Insert quote text')
    parser.add_argument('--author', type=str, required=False, default=None, help='Insert author name')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
