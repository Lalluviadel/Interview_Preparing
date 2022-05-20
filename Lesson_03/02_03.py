"""
Task 2.
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def int_or_float():
    user_num = input('Введите ваше число: ')

    if user_num.isdigit():
        print('Число целое')
    elif user_num.replace('.', '', 1).isdigit():
        print('Число дробное')
        num_parts = user_num.split('.')
        return True if num_parts[0] == num_parts[1] else False
    else:
        print('Введенное вами значение не является числом.')


result = int_or_float()
if result:
    print(result)
