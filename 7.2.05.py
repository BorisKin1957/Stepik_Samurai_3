'''На вход поступает список целых чисел, необходимо оставить только те числа
в которых не встречается сочетания цифр 23. Итоговый список вывести на экран.

Sample Input:

12 23 123 45 67 6723
Sample Output:

[12, 45, 67]'''


numbers = map(int, input().split())

print(list(filter(lambda x: '23' not in str(x), numbers)))