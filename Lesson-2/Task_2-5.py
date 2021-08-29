print("<РЕЙТИНГ>")
my_el = [7, 5, 3, 3, 2]
n = float(input("Введите новый элемент списка: "))
new_el = []
flag = False
for elem in my_el:
    if n >= elem and flag == False:
        new_el.append(n)
        flag = True
    new_el.append(elem)

print(new_el)
