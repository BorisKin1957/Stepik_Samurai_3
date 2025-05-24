import time


def decor_1(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


def decor_2(func):
    def wrapper(n):
        x_1 = time.time()
        f = func(n)
        return f, time.time() - x_1

    return wrapper


def func(n: int) -> int:
    return sum((i ** 3 for i in range(1, n)))


x = decor_2(decor_1(func))

x = decor_2(decor_1(func))
print(x(9999999))
print(x(9999999))
