'''Реализовать следующий код:

func_1()()()()() => "Ну и зачем тебе это?"'''


def func_1():
    def func_2():
        def func_3():
            def func_4():
                def func_5():
                    print('Ну и зачем тебе это?')
                return func_5
            return func_4
        return func_3
    return func_2


func_1()()()()()
