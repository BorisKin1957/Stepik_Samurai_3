'''Напишите функцию func, которая принимает имя файла и целое число.
Данная функция должна выводить в консоль то количество строк, которое вносится
в качестве второго аргумента. '''

def func(file_name: str, n: int) -> None:
    f = open(file_name, 'r', encoding='utf-8')
    for _ in range(n):
        print(f.readline().strip())
    f.close()

func('files/text_1.txt', 3)