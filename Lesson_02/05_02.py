"""
Task 5.
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе
будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать вызов каждой из функции get_info.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self, new_price):
        self.__price = new_price


class ItemDiscountReportName(ItemDiscount):

    def get_info(self):
        return self.get_name


class ItemDiscountReportPrice(ItemDiscount):

    def get_info(self):
        return self.get_price


child_item = ItemDiscountReportName('Лампа Smartbuy', 450)
child_item_2 = ItemDiscountReportPrice('Степлер Silwerhof', 185)


for item in (child_item, child_item_2):
    print(item.get_info())
