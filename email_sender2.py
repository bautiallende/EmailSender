import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'Email'
email['subject'] = 'Email Subject'

email.set_content('Email Content')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Your Email','Password')
    smtp.send_message(email)
    print('all good boss!')