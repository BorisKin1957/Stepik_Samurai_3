'''В глобальном пространстве у вас есть переменная hp = 1000(здоровье Федора).
Вам необходимо создать функцию func, которая принимает список строк. Примеры строк:

'hp -= 250'
'hp += 200'
Строка со знаком "-", это строка кода, ответственная за убыль здоровья(hp),
соответственно строка со знаком "+" за восполнение здоровья. Важно, что здоровье
может находится только в диапазоне 0<hp<=1000. Значит, сколько строк было в списке
столько и потенциального воздействия на hp(атак/лечений). Также каждая вторая
строка со знаком "-" игнорируется. Функция ничего не возвращает, лишь глобально
влияет на переменную hp. Если персонаж погиб, переменная hp будет ссылаться на строку:

Геройски погиб в битве с нечистью.
Последние слова героя: "Фу, косой! Бе-бе-бе не попадешь! Ай, больно! Ребят,
хильте быстрей! Ребята!!!"'''


def func(arr: list):
    '''Фннкция следит за здоровьем лыцаря Феди'''
    neg = False
    for i in arr:
        if '-=' in i:
            neg = not neg
            if neg:
                exec(i, globals())
        else:
            exec(i, globals())
        #print(hp)
        global hp
        if hp <= 0:
            hp = 'Герой погиб в битве с нечистью.\nПоследние слова героя: "Фу, косой! Бе-бе-бе не попадешь! Ай, больно! Ребят, хильте быстрей! Реб'
            break
        elif hp > 1000:
            hp = 1000
    return hp

hp = 1000


func(['hp -= 250', 'hp -= 300', 'hp += 250', 'hp -= 175', 'hp += 200', 'hp -= 300'])
print(hp)

hp = 1000
func(['hp -= 400', 'hp -= 300', 'hp += 350', 'hp -= 575', 'hp += 300', 'hp -= 300'])
print(hp)
hp = 1000
func(['hp -= 500', 'hp += 250', 'hp -= 350', 'hp -= 750', 'hp += 300', 'hp -= 150'])
print(hp)