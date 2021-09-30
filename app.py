import random
import os
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine
import utils
import logging

logger - logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """
    try:
        quotes = open_quote_app()
     except ValueError:
        logger.exception('Default quote files not found')

    try:
        imgs = open_image_app()
    except ValueError:
        logger.exception('Default image files not found')

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    try:
        img = random.choice(imgs)
    except ValueError:
        logger.exception('Could not randomly select an image file')
    try:
        quote = random.choice(quotes)
    except ValueError:
        logger.exception('Could not randomly select an image file')
    try: 
        path = meme.make_meme(img, quote.body, quote.author)
    except Exception as e:
        logger.exception(e)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    tmp = f'./static/{random.randint(0, 1000000)}.jpg'

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    
    if not image_url or not body or not author:
        error = "Fields Cannot Be Empty..."
        return render_template("meme_form.html",
                              error=error,
                              image_url=image_url,
                              body=body,
                              author=author)

    try:
        img_content = requests.get(img_url, stream=True).content
        with open(tmp, 'wb') as f:
            f.write(img_content)
    except Exception as e:
        logger.exception(e)
        error = "Invalid input...Verify URL correct"
        return render_template("meme_form.html",
                              error=error,
                              image_url=image_url,
                              body=body,
                              author=author)

    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
