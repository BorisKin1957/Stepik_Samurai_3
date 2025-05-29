'''создайте функцию func, которая принимает имя файла и выводит в консоль
количество букв, слов и строк. Выведите три найденных числа в формате,
приведенном в примере.

<число> букв
<число> слов
<число> строк'''


def func(file_name: str) -> None:
    f = open(file_name, 'r', encoding='utf-8')
    rows, letters, words = 0, 0, 0
    for line in f:
        lst = [word.strip() for word in line.split() if len(word) > 1 or word.isalpha()]
        rows += 1
        words += len(lst)
        for word in lst:
            letters += len([letter for letter in word if letter.isalpha()])

    print(f'{letters} букв')
    print(f'{words} слов')
    print(f'{rows} строк')

    f.close()


func('files/text_1.txt')
