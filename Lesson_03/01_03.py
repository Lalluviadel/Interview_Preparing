"""
Task 1.
Написать программу, которая будет содержать функцию для получения имени
файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла
с расширением.
В функции необходимо реализовать поиск имени файла (с расширением), а затем
«выделение» имени файла (без расширения).
Расширений может быть несколько (например testfile.tar.gz).
"""


def give_me_filename(path):
    filename_raw = path.split('/')[-1]
    filename = filename_raw.split('.')[0]
    return filename


result = give_me_filename('C:/Users/dns/Desktop/Ucheba/Chetvert 4/'
                          'Interview/Interview Preparing/Lesson_01/01_01.py')
result_2 = give_me_filename('C:/Users/dns/Desktop/Ucheba/Chetvert 4/'
                            'Interview/Interview Preparing/Lesson_01/testfile.tar.gz')
print(result, result_2)
