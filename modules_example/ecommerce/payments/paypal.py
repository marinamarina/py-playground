# I want to use the database package inside the parent package
# Import send mail function into paypal

from ..database import database
from ..contact.email import Email

class Paypal:
    def __init__(self, payment=''):
        self._payment = payment

    @property
    def payment (self):

        return  'Payment is: %s, %s' % (self._payment)

    def useEmailImport(self):
        e = Email('a@s.com')
        print e.sendMail()
