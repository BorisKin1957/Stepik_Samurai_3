'''Создайте вручную файл class_scores.txt с содержимым:

Чубака 65
Немезисов 85
Патрик 95
Зергов 94
Холодцова 80
Улюлюкина 50
Хруст 30
Геннадьевна 87
Файл представляет собой список фамилий  с количеством баллов за тест.
Вам необходимо создать функцию func без параметров, которая считывает данный файл
и создает новый new_scores.txt. В котором к каждому результату добавляется
дополнительные 10 баллов, в том случае если сумма не превысит 100 баллов,
иначе количество баллов остается прежним'''

def func():
    with (open('files/class_scores.txt', 'r', encoding='utf-8') as f_in,
          open('files/new_scores.txt', 'w', encoding='utf-8') as f_out):
        for line in f_in:
            lst = line.split()
            if 10 + int(lst[1]) <= 100:
                lst[1] = str(10 + int(lst[1]))
            f_out.write(' '.join(lst) + '\n')
    # далее излишний код, лишь для наглядности
    with open('files/new_scores.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

func()