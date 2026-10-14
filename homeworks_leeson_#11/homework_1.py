class Product:
    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def get_name(self):
        return self.__name

    def get_shop(self):
        return self.__shop

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.__price + other.__price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.__price < other.__price

    def __str__(self):
        return (
            f'Название: {self.__name}, '
            f'магазин: {self.__shop}, '
            f'цена: {self.__price}'
        )


class Warehouse:
    def __init__(self):
        self.__products = []

    def add(self, product):
        if not isinstance(product, Product):
            raise TypeError('Ожидается объект Product')

        self.__products.append(product)

    def get_by_index(self, index):
        return self.__products[index]

    def get_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return product

        return None

    def sort_by_name(self):
        return sorted(self.__products, key=lambda product: product.get_name())

    def sort_by_shop(self):
        return sorted(self.__products, key=lambda product: product.get_shop())

    def sort_by_price(self):
        return sorted(self.__products)