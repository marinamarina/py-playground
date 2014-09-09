from ecommerce.products import Product
from ecommerce.payments.paypal import Paypal
from ecommerce import database

p1 = Product()
print p1.example()

p2 = Paypal('444')
print p2.useEmailImport()