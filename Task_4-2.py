# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
from random import randint

my_spisok = [randint(0, 300) for el in range(10)]
print(f"Список случайных чисел: {my_spisok}")
my_new_spisok = [my_spisok[i] for i in range(1, len(my_spisok)) if my_spisok[i] > my_spisok[i - 1]]

print(f"Список элементов исходного списка, значения которых больше предыдущего элемента: {my_new_spisok}")
