import smtplib
import EmailConfig as email
import EmailMessage as msg

receiver_email = ['']


def main():
    try:
        server = smtplib.SMTP(email.smtp_server, email.port)
        server.ehlo()  # Can be omitted
        server.starttls()
        server.login(email.from_email, email.password)
        server.sendmail(email.from_email, receiver_email, msg.create_template('',''))
        print "Successfully sent email"
        server.quit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()




