# Определяем внешнюю функцию f_1
def f_1():
    # Инициализируем переменную result
    result: int = 0

    # Определяем внутреннюю функцию f_2, которая принимает число и добавляет его к переменной result
    def f_2(number):
        # используя ключевое слово nonlocal для изменения внешней переменной result
        nonlocal result
        result += number
        return result

    # Возвращаем внутреннюю функцию f_2
    return f_2


x = f_1()
print(x(1), x(2), x(3))

x = f_1()
print(x(3), x(2), x(5))
