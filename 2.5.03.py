from time import sleep

def decor(time_sleep):
    def inner(func):
        def wrapper(**kwargs):
            sleep(time_sleep)
            return func(**kwargs)

        return wrapper

    return inner


def func(**kwargs):
    return kwargs


time_sleep = int(input())
x = decor(time_sleep)(func)
x = x(num_1='одын', num_2='неодын')
print(x)