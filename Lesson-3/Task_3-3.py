# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def summa(a, b, c):
    n_list = {a, b, c}
    n_list.remove(min(n_list))
    return sum(n_list)


print(f'Result: {summa(-45, 3, 2)}')
