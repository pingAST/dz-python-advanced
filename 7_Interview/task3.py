import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:
    def __init__(self, login, password, subject, recipients, message, header=None):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())

        ms.quit()

    def get_email_body(self, msg):
        if msg.is_multipart():
            return '\n'.join([self.get_email_body(part) for part in msg.get_payload()])
        else:
            payload = msg.get_payload(decode=True)
            if isinstance(payload, bytes):
                return payload.decode(msg.get_content_charset())
            else:
                return ''

    def receive_email(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)

        if data[0]:
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            # Вывод информации о письме
            print('From:', email_message['From'])
            print('Subject:', email_message['Subject'])
            print('Body:', self.get_email_body(email_message))
        else:
            print('There are no letters with the current header')

        mail.logout()


if __name__ == '__main__':
    client = EmailClient('login@gmail.com', 'qwerty', 'Subject', ['vasya@email.com', 'petya@email.com'], 'MessageСообщение')
    client.send_email()
    client.receive_email()
