'''Вам необходимо создать функцию func, которая принимает список.
В котором могут находится только экземпляры 2-ух типов: human и infected_human
(это нестандартные типы объектов, созданные исключительно для данной задачи).
Функция должна вернуть кортеж из 3-ёх элементов. Первый статус зараженности
корабля(True/False), 2-ой - количество незараженных членов экипажа(human),
3-ий - количество зараженных(infected_human).  Нужно только объявить функцию.  '''

def func(lst):
    sick, healthy = 0, 0
    for item in lst:
        if isinstance(item,  human):
            healthy += 1
        else:
            sick += 1
    if sick > 0:
        return True, healthy, sick
    else:
        return False, healthy, 0