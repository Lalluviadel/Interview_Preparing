"""
Task 4.
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
в который должна передаваться переменная — скидка), и перегрузку метода
__str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой. Чтобы все работало корректно, не забудьте
инициализировать дочерний и родительский классы (вторая и третья строка
после объявления дочернего класса).
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

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self):
        return f'{self.get_name} {self.get_price}'

    def __str__(self):
        return str(self.get_price - (self.get_price/100*self.discount))


parent_item = ItemDiscount('Лампа Smartbuy', 450)
print(f'{parent_item.get_name} {parent_item.get_price}')

child_item = ItemDiscountReport('Степлер Silwerhof', 185, 21)
print(child_item.get_parent_data())
print(f'Цена товара {child_item.get_name}: {child_item.get_price}, '
      f'цена со скидкой: {child_item}')
