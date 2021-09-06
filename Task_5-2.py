# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('my_file_2.txt', 'r') as my_file_2:
    count = 0
    for line in my_file_2:
        count +=1
        print(f'В строке №{count} {len(line.split())} слов')
    print(f'Всего строк: {count}')