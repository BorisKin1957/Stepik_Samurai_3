'''На вход подается список целых чисел, необходимо отфильтровать все числа кроме
двузначных. Итоговый список вывести на экран.

Sample Input:

1 22 3 44 5 66 7 88
Sample Output:

[22, 44, 66, 88]'''


numbers = map(int, input().split())

print(list(filter(lambda x: len(str(x).replace('-', '')) == 2, numbers)))