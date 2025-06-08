'''Создайте функцию func, которая принимает позиционно список или кортеж.
Если аргументом является список, то она фильтрует его, оставляя в нем только
строчные объекты, если кортеж - то целочисленные. Во всех случаях возвращается список'''

def func(*args):
    for arg in args:
        if isinstance(arg, list):
            return [i for i in arg if isinstance(i, str)]
        return [i for i in arg if isinstance(i, int) and not isinstance(i, bool)]


print(func([1, 'sdf', 6, 'asd']))
print(func((1, 2, 3, 4, 5, True)))
print(func(['cvb', 'dfgh', 5, 7]))
print(func((False, 6, 5, 8)))
print(isinstance(True, int))