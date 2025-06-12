from math import factorial as fact

def func(n):
    if n == 0:
        return 1
    else:
        return fact(n)
x = func