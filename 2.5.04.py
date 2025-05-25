'''Вам нужно создать функцию func, которая принимает строку и изменяет в ней
буквы кириллицы в соответствующие
латинские при помощи словаря, регистр букв в строке игнорируется. Измененная строка
возвращается. Словарь пропишите внутри логики функции. Далее пишем декоратор decor
с параметром repl=None. Аргумент repl может принимать строковое значение,
и если он задан, то он удаляет все равные ему подстроки в итоговой строке.
'''

def decor(repl=None):
    def dec(func):
        def wrapper(*args):
            translit = func(*args)
            if not repl:
                return translit
            else:
                return translit.replace(repl, '')


        return wrapper

    return dec


def func(string: str):
    dct = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
           'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
           'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
           'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    for char in string:
        if char.lower() in dct:
            string = string.replace(char, dct[char.lower()])
    return string


x = decor('е')(func)
print(x('А кто это у нас тут такой с моськой в кетчупе'))

x = decor()(func)
print(x('Ну что вы что вы в прорубь после вас'))

x = decor('k')(func)
print(x('как тебе не стыдно эпидермис видно'))
