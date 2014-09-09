# I want to use the database package inside the parent package

class Email:
    def __init__(self, email=''):
        self._email = email

    @property
    def email (self):

        return  'Email is: %s' % (self._email)

    def sendMail(self):
        return 'Mail is sent. ' + self.email