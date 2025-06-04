def func(unknow):
    if type(unknow) == str:
        return '#' + unknow
    elif type(unknow) == list:
        return '#' + ''.join([str(i) for i in unknow])

def test_func(func, test_lst):
    for i in test_lst:
        print(i[2])
        assert func(i[0]) == i[1], i[2]



test_lst = [
    ['1234', '#1234', '1 тест'],
    [['1', '3', 'a'], '#13a', '2 тест'],
    [['qwsdf4'], '#qwsdf4', '3 тест'],
    [5, None, '4 тест'],
    [('q', 'w', 'd'), None, '5 тест'],
    [[1, True, 'f'], '#1Truef', '6 тест']
]


# print(func(['1', '3', 'a']))

# print(func(1))

test_func(func, test_lst)