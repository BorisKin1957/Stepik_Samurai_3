'''Необходимо создать функцию func без параметров, которая формирует словарь по
принципу: в ключе '10' находится список первых 10ти букв латинского алфавита в
нижнем регистре, в ключе '20' второй десяток букв и т.д. И записывает его в
файл task_2.json. Необходимо только объявить функцию.'''

import json


def func():
    result = {}
    for i in range(0, 27, 10):
        l = []
        for j in range(97 + i, 107 + i):
            if j <= 122:
                l.append(chr(j))
        result[i + 10] = l
    with open('files/task_2.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=6)

func()
