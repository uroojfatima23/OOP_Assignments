# Assignment 18: Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example usage
product = Product(100)
print(product.price)  # Output: 100
product.price = 120
print(product.price)  # Output: 120
del product.price