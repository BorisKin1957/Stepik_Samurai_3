'''Вам необходимо избавиться от всех атрибутов всех элементов в файле inventory.xml.
Файл необходимо перезаписать.'''

# Импортируем модуль ElementTree из модуля xml
import xml.etree.ElementTree as ET

# Парсим файл inventory.xml и сохраняем результат в переменной tree
tree = ET.parse('files/inventory.xml')

# Получаем корневой элемент из дерева tree и сохраняем результат в переменной root
root = tree.getroot()

# Проходим по всем элементам в дереве tree
for elem in tree.iter():
    # Удаляем все атрибуты элемента
    elem.attrib.clear()

# Записываем дерево tree в файл inventory.xml
tree.write('inventory.xml', encoding="utf-8", method="xml")