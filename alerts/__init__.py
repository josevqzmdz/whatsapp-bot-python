from dotenv import load_dotenv
import os, datetime, pytz, smtplib
from email.message import EmailMessage

load_dotenv()
EMAIL_PASS = os.environ['EMAIL_PASS']
SENDER = os.environ['SERVER_EMAIL']
RECIPIENTS = os.environ['PRODUCTION_DEPLOYMENT_SUCCESS_EMAIL_RECIPIENTS']

class Email:
    def __init__(self):
        self.recipients = RECIPIENTS
        self.password = EMAIL_PASS
        self.sender = SENDER
        self.datetime = datetime.datetime.now(pytz.timezone("Mexico/Guadalajara")).strftime("%m/%d/%Y, %H:%M:%S")

    def send_production_deployment_alert(self):
        try:
            msg = EmailMessage()
            msg["Subject"] = "WhatAppp chatbot alert"
            msg["From"] = self.sender
            msg["To"] = self.recipients

            body  f"""
                Hello! A new version of your whatsapp chatbot has been deployed to production at {self.datetime} , GMT-6 local time.

                Do not reply to this email as this is a system-generated notification.

                Best wishes,
                chemiloco

            """
            msg.set_content(body)
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(self.sender, self.password)
                print("log in succesful!! sending email...")
                smtp.send_message(msg)
        except Exception as e:
            raise e: