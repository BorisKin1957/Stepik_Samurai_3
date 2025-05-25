'''Нужно создать функцию func, которая принимает произвольное число аргументов и
возвращает их список. Затем декоратор decor_param, который принимает аргумент ind,
отдекарированная функция должна возвращать срез списка [ind:]. Декорировать и
вызывать ничего не нужно.'''


def decor_param(ind: int) -> list[int]:
    def decor(func: object):
        def wrapper(*args):
            return func(*args)[ind:]
        return wrapper
    return decor

def func(*args: tuple[int]) -> list[int]:
    return list(args)

x = decor_param(2)(func)
print(x(1, 2, 3, 4, 5, 6))

x = decor_param(5)(func)
print(x(1, 2, 3, 4, 5, 6, 7, 8, 9))