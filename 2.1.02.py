def get_incr_number() -> int:
    '''Увеличивает переменную x на 1'''
    global x
    x += 1

x = int(input())

get_incr_number()
print(x)