def func(expr: str):
    '''функция проверяет является ли введенное выражение коллекцией, и является валидным '''
    if expr[0] in '([{' and expr[-1] in ')}]':
        try:
            return eval(expr)
        except (SyntaxError, NameError, TypeError):
            pass
    return 'Вредоносный код'


print(func('1 + 2'))
print(func('1 + 2 +'))
print(func('[1 + 2 -]'))
print(func('([1 + 2] + 3)'))
print(func('[1 + 2]'))
print(func("{1: 'счастье есть?', 2: 'а если найду?'}"))