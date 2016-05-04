from email.mime.text import MIMEText
from smtplib import SMTP


class Gmail(object):
    """Send an email with Google Mail

    Can easily be used with other providers
    by editing the server and port in send()

    Args:
        credentials (tuple): (username, password)
    """
    def __init__(self, credentials):
        self.user, self.password = credentials

    def send(self, receiver, subject, body):
        """Send email

        Args:
            receiver (str): Address of receiver
            subject (str): Subject of email
            body (str): Body of email
        """
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = self.user
        message['To'] = receiver

        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.user, self.password)
        server.sendmail(self.user, receiver, message.as_string())
        server.quit()
