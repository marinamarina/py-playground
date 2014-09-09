class Database:
    def __init__(self, connection=''):
        self._connection = connection

    @property
    def connection (self):
        return  'Connection: %s' % (self._connection)

# delaying initializing of database
database = None

def initialize_database():
    global database
    database = Database(connection='ultimate')