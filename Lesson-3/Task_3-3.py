# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def summa(arg1, arg2, arg3):
    """Возвращает сумму наибольших двух аргументов
    Принимает три числа,
    для некорректных аргументов возвращает None"""
    try:
        n_list = [int(arg1), int(arg2), int(arg3)]
    except ValueError:
        return None
    n_list.remove(min(n_list))
    return sum(n_list)


print(summa(-1, '2', 3))