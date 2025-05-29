'''Напишите функцию func, которая принимает имя файла и выводит в консоль всё
содержимое файла. Вызывать не нужно.'''

def func(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    print(f.read())
    f.close()

func('files/text_1.txt')