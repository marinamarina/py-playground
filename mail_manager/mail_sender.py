import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

'use normal dictionary for the headers instead'
def sendmail(subject, message, from_add, headers = None, *to_add):

    headers = None if headers == None else headers
    host = 'localhost'
    port = '25'
    email = MIMEText(message)
    email['From'] = from_add
    email['Subject'] = subject


    sender = smtplib.SMTP(host, port)
    for recepient in to_add:
        del(email['To'])
        email['To'] = recepient
        sender.sendmail(from_add, recepient, email.as_string())
    sender.quit()

class MailingList:
    def __init__(self):
        self.email_map = defaultdict(set)

    def add_email_to_group(self, mail, group):
        self.email_map[mail].add(group)


sendmail("A model subject", "The message contents", "from@example.com", "to1@example.com", "to2@example.com")