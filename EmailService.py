import smtplib
import EmailConfig as email
import EmailMessage as msg


def send_email(user_email, matched_user):
    try:
        server = smtplib.SMTP(email.smtp_server, email.port)
        server.ehlo()  # Can be omitted
        server.starttls()
        server.login(email.from_email, email.password)
        server.sendmail(email.from_email, user_email, msg.create_email(matched_user))
        print("Done did send")
    except Exception as e:
        print(e)


def main(user_list):
    for key, value in user_list.items():
        send_email(key, value)


if __name__ == '__main__':
    main()




