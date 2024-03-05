import os
import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = os.environ.get('EMAIL_PASSWORD')
SENDER = os.environ.get('EMAIL_ADDRESS')
RECEIVER = os.environ.get('EMAIL_ADDRESS')

def send_email(image_path):
    email_message = EmailMessage()
    email_message['Subject'] = 'Motion Detected!'
    email_message.set_content('Hey, we just detected motion on the webcam')

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
