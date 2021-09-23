import os
import smtplib
import imghdr
from email.message import EmailMessage
  
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def mail_meme(self, file, recipient, sender):
  self.file = file
  self.recipient = recipient
  self.sender = sender
  
  msg = EmailMessage()
  msg['Subject'] = 'Check out this awesome meme!'
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = email
  msg.set_content('Meme attached...')
  
  with open(self.file, 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(self.file)
    file_name = f.name
  
  msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name
  
  with smtplib.SMTP_SSL(smtp.gmail.com, 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
