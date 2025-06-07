'''Нужно написать функцию func с произвольным количеством позиционных параметров,
которая возвращает их кортеж. Создать декоратор gen_decor, который преобразует
функцию в генератор, так чтобы при обращении к ней, она последовательно выдавала
элементы кортежа.'''

def gen_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for item in result:
            yield item
    return wrapper


def func(*args):
    '''функция возвращает их кортеж'''
    return args

# Применяем декоратор gen_decor к функции func и сохраняем результат в переменной x
x = gen_decor(func)

gen = x(5.6, 6.5, 2)

print(next(gen))  # 5.6
print(next(gen))  # 6.5
print(next(gen))  # 2
