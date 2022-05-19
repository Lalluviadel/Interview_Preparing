"""
Task 2.
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет
сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к
защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
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


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.get_name} {self.get_price}'


parent_item = ItemDiscount('Лампа Smartbuy', 450)

try:
    print(f'{parent_item.name} {parent_item.price}')
except AttributeError:
    print('Попытка доступа к защищенным параметрам!')

print(f'{parent_item.get_name} {parent_item.get_price}')

child_item = ItemDiscountReport('Степлер Silwerhof', 185)
print(child_item.get_parent_data())
