# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
print("<РЕЙТИНГ>")
my_el = [7, 5, 3, 3, 2]
while True:
    in_value = int(input('Введите новый элемент рейтинга: '))

    if my_el[-1] > in_value:
        my_el.append(in_value)
    elif my_el[0] < in_value:
        my_el.insert(0, in_value)
    else:
        for el in my_el:
            if in_value > el:
                my_el.insert(my_el.index(el), in_value)
                break
    print(my_el)
