"""
Разработать целочисленный генератор случайных чисел.
В функцию передавать начальную и конечную границу диапазона генерации
(выдавать значения из диапазона включая концы).
Заполнить этими данными словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”,
а значение - сгенеренное случайное число.  Вывести содержимое словаря.
"""
from random import randint


def simple_gen(start_num, end_num, quantity=20, counter=1):
    result_dict = {}
    while len(result_dict) < quantity:
        rand_int = randint(start_num, end_num)
        result_dict[f'elem_{counter}'] = rand_int
        counter += 1
    return result_dict


print(simple_gen(1, 50))

"""
(Усложненный вариант по желанию*): Не использовать стандартный модуль python
random.

-----
Я использовала линейный конгруэнтный генератор и тот факт, что множество в
Python является неупорядоченным набором элементов. В итоге получаем некий
самодельный генератор псевдослучайных чисел. Словарь может получать и повторяющиеся
значения, я проверила. При каждом запуске скрипта получаем уникальный словарь.
"""


def lc_gen(start_num, end_num, quantity=20, counter=1):
    def rng(m=2 ** 32, a=1103515245, c=12345):
        rng.current = (a * rng.current + c) % m
        return rng.current / m
    rng.current = 1

    result_dict = {}
    temp_set = set()
    for i in range(quantity*10):
        temp_set.add(str(rng()))
    while len(result_dict) < quantity:
        elem = int(float(temp_set.pop()) * end_num + 1)
        if elem >= start_num:
            result_dict[f'elem_{counter}'] = elem
            counter += 1
    return result_dict


print(lc_gen(30, 50))
print(lc_gen(1, 100))
