# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

slova = input("Напишите слова через пробел: ")
x = slova.split(' ')
for i, slovo in enumerate(x, 1):
    if len(slovo) > 10:
        slovo = slovo[0:10]
    print(f"{i} - {slovo}")