'''Необходимо создать функцию func, которая принимает строку из различных букв,
цифр и символов. Функция возвращает эту строку, но оставляет в ней только числовые
значения, все остальное удаляется. Далее необходимо создать декоратор decor,
который принимает целое число в качестве аргумента. Суть декоратора, в том что
он кеширует результат функции в один из двух списков. В первом списке все результаты,
длины которых менее аргумента декоратора, в остальном другие.
Декоратор должен возвращать строку вида:

Список объектов длиной менее <длина> - [...]
Список остальных объектов - [...]'''


def decor(n: int):
    def inner(func):
        cache_short, cache_long = [], []

        def wrapped(string):
            new = func(string)
            if len(new) < n:
                cache_short.append(new)
            else:
                cache_long.append(new)
            return (f'Список объектов длиной менее {n} - {cache_short}\n'
                    f'Список остальных объектов - {cache_long}')

        return wrapped

    return inner


def func(string: str) -> str:
    for char in string:
        if not char.isdigit():
            string = string.replace(char, '')
    return string


x = decor(5)(func)
print(x('1w3er2df4'))
print(x('1w3er2df547'))
print()
x = decor(7)(func)
print(x('5hf8ghj6he8'))
print(x('b^83fg6459347ghbn5'))
