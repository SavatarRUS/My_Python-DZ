# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('my_file.txt', 'w')

while True:
    user_text = input('Введите новую строку: ')
    if user_text == '':
        break
    my_file.writelines(user_text + '\n')

my_file.close()
