'''На вход подается произвольное количество целых чисел в одну строку через пробел
Sample Input 1:
1 2 3 4 5
Sample Output 1:
3.0'''

numbers = list(map(int, input().split()))

# Определяем функцию для вычисления среднего арифметического чисел в списке
arithmetic_mean = lambda x: sum(x) / len(x)

print(arithmetic_mean(numbers))