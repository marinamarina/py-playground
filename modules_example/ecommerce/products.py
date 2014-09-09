from .database import database

class Product:

    def __init__(self, price=0):
        self._price = price

    @property
    def price (self):
        return  'Product price: %s' % (self._price)

    def example (self):
        return self.price
