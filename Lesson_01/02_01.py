"""
Task 2.
Реализовать функцию print_directory_contents(path).
Функция принимает имя директории и выводит ее содержимое,
включая содержимое всех поддиректории (рекурсивно вызывая саму себя).
Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""
import os


def print_directory_contents(path, is_nested=False):
    if os.path.exists(path):
        current_content = os.listdir(path)
        print(f'Вложенная папка {path}: ') if is_nested else print(f'Папка {path}: ')
        folder_storage = []
        for i in current_content:
            item_path = os.path.join(path, i)
            print(i) if os.path.isfile(item_path) else folder_storage.append(item_path)
        print('-----')
        for folder in folder_storage:
            print_directory_contents(folder, is_nested=True)
        return
    print('Указанной директории не существует!')
    return


print_directory_contents('C:/Users/dns/Desktop/Ucheba/Chetvert 4')
