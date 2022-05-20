"""
Task 3.
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Если есть значения, которым не хватило ключей, их необходимо отбросить.
"""
from random import randint


def create_test_dict():
    while True:
        list_keys = [i for i in range(randint(5, 20))]
        list_values = [i for i in range(randint(5, 20))]
        len_keys, len_values = len(list_keys), len(list_values)
        if len_keys != len_values:
            break

    if len_keys > len_values:
        difference = len_keys - len_values
        list_values += [None] * difference
    result = {k: v for k, v in zip(list_keys, list_values)}

    print(list_keys)
    print(list_values)
    print(result)


create_test_dict()
