# this file sends an email whenever the docker container is updated

from dotenv import load_dotenv
import os, datetime, pytz, smtplib
from email.message import EmailMessage

load_dotenv()
EMAIL_PASS = os.environ['EMAIL_PASS']
SENDER = os.environ['SERVER_EMAIL']
RECIPIENTS = os.environ['SANITY_CHECK_EMAIL_RECIPIENTS']

class Email:
    def __init__(self):
        self.recipients = RECIPIENTS
        self.password = EMAIL_PASS
        self.sender = SENDER
        '''
        set timezone
        notice that with "etc", the symbol is inverted (GMT-6 equals GMT+6)
        '''
        self.datetime = datetime.datetime.now(pytz.timezone("Etc/GMT+6")).strftime("%m/%d/%Y, %H:%M:%S")

    def send_production_deployment_alert(self):
        try:
            msg = EmailMessage()
            msg["Subject"] = "WhatsApp Bot Sanity Check"
            msg["From"] = self.sender
            msg["To"] = self.recipients

            body = f"""
            Hello Chemi,

            A new docker image has been tested and pushed to production at {self.datetime}.

            Do not reply to this email as this is a system-generated email.

            Kind regards,
            Chemi
            """

            msg.set_content(body)

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(self.sender, self.password)
                print("log in successful! sending mail!")
                smtp.send_message(msg)

        except Exception as e:
            raise e