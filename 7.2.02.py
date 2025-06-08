'''На вход подается список целых чисел. Необходимо преобразовать каждый элемент
в среднее арифметическое этого списка, при условии если бы этого элемента не было.
Вывести итоговый список на экран.'''


def func(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        tmp = numbers.copy()
        tmp.remove(number)
        result.append(sum(tmp) / len(tmp))
    return result

lst_int = list(map(int, input().split()))

print(func(lst_int))