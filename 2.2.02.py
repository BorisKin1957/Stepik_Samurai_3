''' Надо создать lambda-функцию, которая принимает целое число и определяет
является ли оно кратным 13 или 4. Если да, то возвращается True, иначе False'''

is_multiple_4_13 = lambda x: True if x % 4 == 0 or x % 13 == 0 else False

print(is_multiple_4_13(int(input())))