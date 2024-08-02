from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.\n'

class Shop(Product):

    def __init__(self):
        self.__file_name = 'products.txt'


    def get_products(self):
        self.S = ''
        file = open(self.__file_name, 'r')
        pprint(file.read())
        for b in file:
            self.S += b
        file.close()
        return self.S

    def add(self, *products):
        file = open(self.__file_name, 'a')
        self.get_products()
        for p in products:
            if p.name in self.S:
                print(f'Продукт {self.name} уже есть в магазине')
            else:
                file.write(Product.__str__(p))
        file.close()


# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
# и возвращает единую строку со всеми товарами из файла __file_name.


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
