'''Напишите функцию func, которая принимает имя файла и строку для записи.
Соответственно данная функция создает файл с переданным ей именем и записывает
переданную ей строку'''

def func(file_name: str, string: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(string)

func('files/w+_text.txt', input())