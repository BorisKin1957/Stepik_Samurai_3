'''Вам дан словарь dct. Вам необходимо создать функцию func без параметров,
которая преобразует данный словарь в json-строку и вернет ее.'''


import json

def func():
    return json.dumps(dct, indent=4)


dct = {
    'order_id': 57265,
    'buyer_name': 'Тимур Лемуров',
    'shopperEmail': 'king_julian@gmail.com',
    'contents': [
        {
            'prdct_id': 462,
            'prdct_name': 'Огурчики от дяди Вани',
            'cost': 250,
            'quantity': 1,
        },
        {
            'productID': 23,
            'productName': 'Подливка',
            'cost': 168,
            'quantity': 3,
        }
    ],
    'order_status': 'sending'
}

print(func())