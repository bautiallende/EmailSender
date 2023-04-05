# Python Email Sender

This program demonstrates how to send emails using Python and the `smtplib` library. There are three example Python scripts, each showing a different approach to sending an email. An HTML template is also included for sending emails with HTML content.

## Requirements

- Python 3.x
- A Gmail account with "Allow less secure apps" enabled. [Learn how to enable it here](https://support.google.com/accounts/answer/6010255?hl=en).

## Usage

1. Clone the repository:

git clone https://github.com/bautiallende/EmailSender.git
cd python-email-sender


2. Update the following information in each Python script (`email_sending_html.py`, `email_sender.py`, and `email_sender2.py`):

- Replace `'Your Mail'` and `'Password'` with your Gmail email address and password, respectively.
- Replace `'Name'` with your name or any desired sender name.
- Replace `'Email'` with the recipient's email address.

3. Run any of the Python scripts to send an email:

```bash
python email_sending_html.py

or

python email_sender.py

or 

python email_sender2.py
```
4. After running the script, you should see the message all good boss! printed in the console, indicating that the email was sent successfully.

## Files

* email_sending_html.py: Sends an email using an HTML template (index.html).
* email_sender.py: Sends an email with plain text content.
* email_sender2.py: Another example of sending an email with plain text content.
* index.html: An HTML template for the email content.

## Disclaimer
Please note that sending emails with this method might not be suitable for production environments, and it is recommended to use a proper email service provider for more reliable and secure email delivery.
