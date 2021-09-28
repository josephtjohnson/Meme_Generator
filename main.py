from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine
import argparse
import random
import os
import PIL


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']

        quotes = []
        for f in quote_files:
            try:
                quotes.extend(Ingestor.parse(f))
            except Exception as e:
                print(e)
        
        quote = random.choice(quotes)

    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate a meme!')
    parser.add_argument('--path', type=str, required=False, default=None,
                        help='Insert path to image file')
    parser.add_argument('--body', type=str, required=False, default=None,
                        help='Insert quote text')
    parser.add_argument('--author', type=str, required=False, default=None,
                        help='Insert author name')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
