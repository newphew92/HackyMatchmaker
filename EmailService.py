import smtplib
import json
import EmailConfig as email
import EmailMessage as msg



def readMailList():
    with open('SalMailingList.csv', mode='r') as dataFile:
    # with open('testSet.csv', mode='r') as dataFile:
        # csvReader = csv.DictReader(dataFile)
        for row in dataFile:
            # print (row)
            obj = json.loads(row)
            # print (obj.keys()[0])
            print(obj.values()[0])
            send_email(obj.keys()[0], obj.values()[0])


# def send_email(user_email, matched_users):
def send_email():
    try:
        server = smtplib.SMTP(email.smtp_server, email.port)
        server.ehlo()  # Can be omitted
        server.starttls()
        server.login(email.from_email, email.password)
        with open('SalMailingList.csv', mode='r') as dataFile:
        # with open('testSet.csv', mode='r') as dataFile:
            # csvReader = csv.DictReader(dataFile)
            lineCount = 0
            for row in dataFile:
                if lineCount < 87:
                    lineCount += 1
                    continue
                # print (row)
                obj = json.loads(row)
                # print (obj.keys()[0])
                print(obj.values()[0])
                # send_email(obj.keys()[0], obj.values()[0])
                server.sendmail(email.from_email, obj.keys()[0], msg.create_email(obj.values()[0]))
                lineCount += 1
        print("Done did send")
    except Exception as e:
        print(e)

send_email()
# def main(user_list):
#     for key, value in user_list.items():
#         send_email(key, value)

# readMailList()

# if __name__ == '__main__':
#     main()




