"""
Task 3.
Реализовать возможность переустановки значения цены товара в
родительском классе.
Проверить, распечатать информацию о товаре.
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


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.get_name} {self.get_price}'


parent_item = ItemDiscount('Лампа Smartbuy', 450)
print(f'{parent_item.get_name} {parent_item.get_price}')

parent_item.get_price = 600
print(f'{parent_item.get_name} {parent_item.get_price}')

child_item = ItemDiscountReport('Степлер Silwerhof', 185)
print(child_item.get_parent_data())
