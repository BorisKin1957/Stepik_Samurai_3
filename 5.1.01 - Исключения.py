'''Задаются 2 числа в одну строку через пробел. Необходимо вывести результат
деления на экран, при делении на 0 обработать конкретную ошибку и выводить на
экран 'Деление на ноль'.

Sample Input 1:

1 5
Sample Output 1:

0.2'''

try:
    a, b = [int(i) for i in input().split()]
    print(a / b)
except ZeroDivisionError:
    print('Деление на ноль!')
except ValueError:
    print('Неверное значение!')
