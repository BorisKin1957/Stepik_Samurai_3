char = input()

# Определяем функцию для проверки, является ли символ латинской буквой
is_latin_char = lambda result: True if ord('a') <= ord(char.lower()) <= ord('z') else False

print(is_latin_char(char))