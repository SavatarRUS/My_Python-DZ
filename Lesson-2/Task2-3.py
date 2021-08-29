# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

my_list = ['зима', 'весна', 'лето', 'осень']
my_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
mount = (int (input('Ведите номер месяца: ')))
if mount == 12 or mount == 1 or mount == 2:
    print('"List" Время года: ', my_list[0])
    print('"Dict" Время года: ', my_dict[1])
elif mount == 3 or mount == 4 or mount == 5:
    print('"List" Время года: ', my_list[1])
    print('"Dict" Время года: ', my_dict[2])
elif mount == 6 or mount == 7 or mount == 8:
    print('"List" Время года: ', my_list[2])
    print('"Dict" Время года: ', my_dict[3])
elif mount == 9 or mount == 10 or mount == 11:
    print('"List" Время года: ', my_list[3])
    print('"Dict" Время года: ', my_dict[4])
else:
    print("Такого месяца не существует")