'''Создайте в своем проекте файл task_3.json с содержимым: [куча букв]
Изучите его. Далее вам необходимо создать функцию func без параметров,
которая считает данный файл, преобразует его в python-объект.
Необходимо найти продавца, который продал товаров на большую сумму.
Функция должна вернуть результат в формате списка:

[<имя>, <фамилия>, <сумма проданного товара>]'''


import json


def func():
    lst = []
    with open('files/task_3.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        for item in data:
            total = []
            for products in item['товары']:
                total.append(int(products['сумма']))
            lst.append([item['продавец']['имя'], item['продавец']['фамилия'], sum(total)])
        return max(lst, key=lambda x: x[2])


print(func())