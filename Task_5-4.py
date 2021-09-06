# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

new_file_4 = []
eng_to_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('my_file_4.txt', 'r', encoding='utf-8') as my_file_4:
    for line in my_file_4:
        line = line.split(' ', 1)
        new_file_4.append(eng_to_rus[line[0]] + '  ' + line[1])

with open('my_file_4_new.txt', 'w', encoding='utf-8') as my_file_4_new:
    my_file_4_new.writelines(new_file_4)
