'''Из модуля string импортируйте переменные: ascii_lowercase, ascii_uppercase, punctuation.
Придумайте им сокращенные имена. Выведите их на экран в следующем порядке:
символы, верхний регистр букв, нижний регистр букв. Выводите каждую переменную с новой строки.'''


from string import  ascii_lowercase as lower, ascii_uppercase as upper, punctuation as punc

print(punc, upper, lower, sep='\n')