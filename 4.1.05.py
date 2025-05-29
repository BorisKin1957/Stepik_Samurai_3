'''оздайте функцию func, которая принимает имя файла и выводит все строки файла
в порядке от последней к первой.'''


def func(file_name: str) -> None:
    f = open(file_name, 'r', encoding='utf-8')
    for line in f.readlines()[::-1]:
        print(line.strip())
    f.close()



func('files/text_1.txt')