class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def name(self):
        return 'Product is {}'.format(self.__name)
    
    def price(self):
        return '{0:.2f} $'.format(self.__price)
    
    def quantity(self):
        return '{}'.format(self.__quantity)
    
    def new_product(self, new_product):
        new_name, new_price, new_quantity = new_product.split(' ')
        self.__name = new_name
        self.__price = new_price
        self.__quantity = new_quantity

    

