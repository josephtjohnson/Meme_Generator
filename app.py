import random
import os
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for quote in quote_files:
        quotes.extend(Ingestor.parse(quote))

    images = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    tmp = f'./static/{random.randint(0, 1000000)}.jpg'

    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    if img_url is not None:
        img_content = requests.get(img_url, stream=True).content
        with open(tmp, 'wb') as f:
            f.write(img_content)
    else:
        raise FileNotFoundError('Must provide image url')

    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
