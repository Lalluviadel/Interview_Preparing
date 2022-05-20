"""
Task 4.
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение
и завершаем работу.

Необходимо открыть файл и создать два списка:
с текстовой и числовой информацией.
Для создания списков использовать генераторы.
Применить к спискам функцию zip().

Результат выполнения этой функции должен быть обработан и записан в файл
таким образом, чтобы каждая строка файла содержала текстовое и числовое
значение (например example345).

Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой,
построчный вывод содержимого.
"""


def read_txt(txt_file):
    with open(txt_file.name, 'r', encoding='utf-8') as txt:
        for line in txt:
            print(line.rstrip())


def create_txt(filename):
    msg = 'Файл с таким именем уже существует!'
    try:
        txt = open(filename, 'x')
        txt.close()

        with open(filename, 'w', encoding='utf-8') as txt_file:
            list_abc = [i for i in msg.split()]
            list_num = [list_abc.index(i) for i in list_abc]
            list_mix = list(zip(list_abc, list_num))
            txt_file.writelines(list(map(lambda i: i[0] + str(i[1]) + '\n', list_mix)))
        read_txt(txt_file)
    except FileExistsError:
        print(msg)


create_txt('test.txt')
