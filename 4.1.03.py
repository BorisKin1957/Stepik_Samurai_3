'''Напишите функцию func, которая принимает имя файла и выводит на экран
предпоследнюю строку текста.'''

def func(file_name: str) -> None:
    f = open(file_name, 'r', encoding='utf-8')
    print(f.readlines()[-2].strip())
    f.close()

func('files/text_1.txt')