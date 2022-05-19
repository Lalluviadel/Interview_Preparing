"""
Task 1.
Вывести таблицу умножения в виде:
1 x 1 = 1
1 x 2 = 2

1 x 10 = 10
—
2 x 1 = 2
2 x 2 = 4
…
N x 10 = 10N

Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию)
Между разделами вывести разделитель в виде 5 дефисов
"""


def mult_table():
    while True:
        user_num = input('Введите конечный множитель: ')
        if user_num.isdigit():
            user_num = int(user_num)
            break
    for i in range(1, user_num+1):
        for j in range(1, 11):
            print(f'{i} x {j} = {i*j}')
        print('-----')


mult_table()
