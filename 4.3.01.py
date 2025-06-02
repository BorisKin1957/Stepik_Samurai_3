'''Создайте в проекте файл task_2.csv с содержимым:

секретный-код-для
взлома-пентагона-qwerty123
Нужно создать функцию func без параметров, которая считывает в файле task_2.csv
первое и последнее слово и возвращает их кортежем'''

import csv

def func():
    with open('files/task_2.csv', encoding='utf-8') as csvfile:
        file_reader = list(csv.reader(csvfile, delimiter='-'))
        return file_reader[0][0], file_reader[-1][-1]


print(func())