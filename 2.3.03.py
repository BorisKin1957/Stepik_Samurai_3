def f_1(num_outer):
    # Определяем внутреннюю функцию f_2, которая принимает число и умножает его на значение внешней переменной num_outer
    def f_2(num_inner):
        return num_outer * num_inner

    # Возвращаем внутреннюю функцию f_2
    return f_2


x = f_1(3)
print(x(3))
