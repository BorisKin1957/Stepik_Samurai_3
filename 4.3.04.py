'''Создайте функцию func без параметров, которая создаст файл task_4.csv.
В котором в первой строке будут первые пять цифр, начиная с 1, во второй строке
следующие пять цифр, начиная с 6 и т.д. Последней цифрой в файле должна быть 50.
'''

import csv


def func():
    with open('files/task_4.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(1, 50, 5):
            l = []
            for j in range(i, i + 5):
                l.append(j)
            writer.writerow(l)


func()