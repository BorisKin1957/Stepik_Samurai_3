def decorator(func):
    def wrapper():
        print('Ну сейчас начнется')
        func()
        print('А я предупреждал')

    return wrapper


@decorator
def original_function():
    print('Всё я запустилась')


original_function()
