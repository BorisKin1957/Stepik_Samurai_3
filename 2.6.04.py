'''Вам дан список словарей. Каждый словарь представляет собой игру и информацию
о ней. Вам необходимо отсортировать все игры в порядке убывания их стоимости.
Вам необходимо вывести только игры для PS5 в столбик в определенном формате:

Консоль: PS5, игра: <игра>, цена: <цена>'''

models = [{'console': 'PS5', 'game': 'Uncharted: Legacy of Thieves Collection', 'price': 2399},
          {'console': 'Xbox Series', 'game': "Assassin's Creed Valhalla", 'price': 2950},
          {'console': 'PS5', 'game': "Marvel's Spider-Man 2", 'price': 8799},
          {'console': 'PS5', 'game': 'Hogwarts Legacy', 'price': 6299},
          {'console': 'Xbox Series', 'game': 'Grand Theft Auto: The Trilogy', 'price': 2999},
          {'console': 'PS5', 'game': 'Mortal Kombat 1', 'price': 7699},
          {'console': 'Xbox Series', 'game': 'The Callisto Protocol', 'price': 3899}]

results = sorted(models, key=lambda x: x['price'], reverse=True)

for item in results:
    if item['console'] == 'PS5':
        print(f'Консоль: PS5, игра: {item["game"]}, цена: {item["price"]}')