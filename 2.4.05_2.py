import time


# Декоратор кэширования результатов
def decor_1(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


# Декоратор замера времени выполнения
def decor_2(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        duration = end - start
        return result, duration

    return wrapper


# Основная функция — сумма кубов от 1 до n (не включая n)
def func(n):
    return sum(i ** 3 for i in range(1, n))


# Пример использования
x = decor_2(decor_1(func))
print(x(9999999))
print(x(9999999))
