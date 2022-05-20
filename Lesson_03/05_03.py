"""
Task 5.
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно)
заменить на значения типа 345example (в обратном порядке, число и строка).

Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.

Реализовать функцию-замену всех найденных подстрок на новое значение и
вывод измененных строк.
"""
import random


def read_txt(txt_file):
    with open(txt_file.name, 'r', encoding='utf-8') as txt:
        for line in txt:
            print(line.rstrip())


def find_str_txt(txt_file, substring, find_first=False, counter=1):
    print('\nЗадано условие: найти первое вхождение.') if find_first \
        else print('\nЗадано условие: найти все вхождения.')

    with open(txt_file.name, 'r', encoding='utf-8') as txt:
        for line in txt:
            if substring in line:
                if find_first:
                    print(f'Найдено первое вхождение "{substring}"'
                          f' в строке {line.rstrip()}')
                    break
                else:
                    print(f'Найдено {counter} вхождение "{substring}"'
                          f' в строке {line.rstrip()}')
                    counter += 1


def replace_str_txt(txt_file, substring, new_substring):
    with open(txt_file.name, 'r', encoding='utf-8') as txt:
        txt_data_list = [line for line in txt]

    with open(txt_file.name, 'w', encoding='utf-8') as txt:
        print('\nИзмененные строки:')
        for line in txt_data_list:
            if substring in line:
                line = line.replace(substring, new_substring)
                print(line.rstrip())
            txt.write(line)


def create_txt(filename):
    msg = 'Файл с таким именем уже существует!'
    try:
        txt = open(filename, 'x')
        txt.close()

        with open(filename, 'w', encoding='utf-8') as txt_file:
            list_abc = [i for i in msg.split()]
            list_num = [list_abc.index(i) for i in list_abc]
            list_mix = list(zip(list_abc, list_num))

            for i in list_mix:
                flag = random.getrandbits(1)
                if flag:
                    txt_file.write(i[0] + str(i[1]) + '\n')
                else:
                    txt_file.write(str(i[1]) + i[0] + '\n')

        read_txt(txt_file)
        find_str_txt(txt_file, 'им', find_first=True)
        find_str_txt(txt_file, 'им')
        replace_str_txt(txt_file, 'им', 'кря')

    except FileExistsError:
        print(msg)


create_txt('test_2.txt')
