from config import mail, \
                  Message


def sent_mail(address: str,
              heading: str,
              text: str = '',
              html: str = '') -> None:

    msg = Message(heading, recipients=[address])
    msg.body = text
    msg.html = html
    mail.send(msg)
