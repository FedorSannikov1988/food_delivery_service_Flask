"""
This module is responsible for sending emails to users.
"""
from config import mail
from flask_mail import Message


def sent_mail(address: str,
              heading: str,
              text: str = '',
              html: str = '') -> None:
    """
    Function for sending an email.

    :param address: str -> the recipient's email address
    :param heading: str -> the recipient's email address
    :param text: str (optional) -> the plain text content of the email
    :param html: str (optional) -> the HTML content of the email
    :return: None
    """

    msg = Message(heading, recipients=[address])
    msg.body = text
    msg.html = html
    mail.send(msg)
