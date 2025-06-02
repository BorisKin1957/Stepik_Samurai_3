'''Создайте в своем проекте файл task_3.csv с содержимым:

name,position,salary
Kwiki Ivanov,curdled milk taster,20000
Alex Baggins,capybara trainer,45000
Grigorii Fox,caries mannequin,11000
Вам необходимо создать функцию func без параметров, которая считывает информацию
с этого файла и формирует список словарей, где самая верхняя строка - это ключи
во всех словарях, остальные строки содержат в себе значения ключей под которыми
они находятся. Список словарей необходимо отсортировать по ключу "salary".
Этот список она и выводит на экран.'''

import csv


def func():
    result = []
    with open('files/task_3.csv', encoding='utf-8') as csvfile:
        file_reader = csv.DictReader(csvfile)
        for row in file_reader:
            result.append(row)
        sorted_result = sorted(result, key=lambda row: row['salary'])
        print(sorted_result)



func()