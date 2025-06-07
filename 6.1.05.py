'''Нужно создать функцию-генератор func_gen, которая принимает в себя целое число
и при обращении к ней генерируется пароль соответствующей длины. Обращаться к
генератору можно неограниченное количество раз и каждый раз получать пароль. В
ам даны наборы символов, которые можно использовать при генерации и функция randint,
которая вам поможет в решении. '''


from random import randint
from string import ascii_letters

def func_gen(number):
    while True:
        password = ''
        for i in range(number):
            password += symb[randint(0, len(symb) - 1)]
        yield password


symb = ascii_letters + "0123456789!?@#$*"

x = func_gen(10)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print()
for _ in range(100):
    print(_)
    print(next(x))