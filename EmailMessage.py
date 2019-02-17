from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import EmailConfig as email


def create_email(matched_user):
    try:
        msg = MIMEMultipart()
        msg['From'] = email.from_email
        msg['Subject'] = 'You have a match! Time to shoot your shot!'
        text = "Congrats! You've matched with " + matched_user + "!"
        msg.attach(MIMEText(text))
        return msg.as_string()
    except Exception as e:
        print("Message broke", e)
