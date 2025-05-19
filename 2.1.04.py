def get_nonlocal_variable():
    '''Функция создает глобальную переменную с именем x
    и присваивает ей значение, которое вводит пользователь.'''
    global x
    x = input()


get_nonlocal_variable()
print(x)