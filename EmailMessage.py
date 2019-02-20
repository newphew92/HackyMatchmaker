from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import EmailConfig as email


def create_email(matched_users):
    try:
        msg = MIMEMultipart()
        msg['From'] = email.from_email
        msg['Subject'] = 'You have a match! Time to shoot your shot!'
        text = "Congrats! You've matched with:\n" + "\n"
        for user in  matched_users:
        	print (user)
        	text+=user
        	text+="\n\n"

        text+= "Need an opening line? Use this generic one: Hey we got matched by the firesale on SAL! Wanna chat?"
        msg.attach(MIMEText(text))
        return msg.as_string()
    except Exception as e:
        print("Message broke", e)
