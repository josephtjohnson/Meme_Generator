import random
import os
import requests
import smtplib
from flask import Flask, render_template, abort, request
from Ingestors import Ingestor
from QuoteEngine import MemeEngine
################################################
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
################################################
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

    images_path = "./_data/photos/dog/"

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
    body = requests.form.get('body')
    author = request.form.get('author')
    
    send_email = input('Email to a friend? Enter Yes or No: ')
    if type(send_email) not 'yes' or not 'no':
      send_email = input('Please try again: Enter Yes or No: ')
    if send_email.lower() = 'yes':
      email = request.form.get('recipient email')
    else:
      pass    
    
 #######################################################
    with smtplib.SMTP('smtp.gmail.com, 587) as smtp:
      smtp.ehlo()
      smtp.starttls()
      smtp.ehlo()
      smtp.login('EMAIL_ADDRESS, EMAIL_PASSWORD) #app password created through app password page
      message = (f'Your friend at {email} sent you a meme!')
      smtp.sendmail(EMAIL_ADDRESS, email, message)
###########################################################    
    if img_url is not None:
        img_content = request.get(img_url,stream=True).content
        with open(tmp,'wb') as f:
            f.write(img_content)
    else:
        raise FileNotFoundError('Must provide image url')
    
    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)
                  
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
