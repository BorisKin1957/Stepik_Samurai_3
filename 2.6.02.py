'''Дан список характеристик в виде строк, в которых указано название скилла и
его значение, необходимо отсортировать его по убыванию значения скилла.
Вывести элементы списка в столбик.

Sample Input:

Sample Output:

stamina 150
health 100
magicka 95
regeneration 3'''

skills = ['health 100', 'magicka 95', 'stamina 150', 'regeneration 3']

print('\n'.join(sorted(skills, key=lambda x: int(x.split()[1]), reverse=True)))