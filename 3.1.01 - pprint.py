'''Попробуйте вывести на экран данный список

lst = [
        {'id': 1, 'username': 'nagibator777', 'password': '23.03.2002'},
        {'id': 2, 'username': 'oladushek', 'password': 'h23234hgi'},
        {'id': 3, 'username': 'batja88', 'password': 'gh&56*9kutU'}
      ]
при помощи функции pprint в одноименном модуле. '''

import pprint

lst = [
        {'id': 1, 'username': 'nagibator777', 'password': '23.03.2002'},
        {'id': 2, 'username': 'oladushek', 'password': 'h23234hgi'},
        {'id': 3, 'username': 'batja88', 'password': 'gh&56*9kutU'}

        ]

pprint.pprint(lst, indent=2)
