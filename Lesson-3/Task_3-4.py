# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    try:
        result = x ** y
    except TypeError:
        return "Ошибка, введите значения заново"
    return result


result = my_func1(1, -7)
print(f"Результат: {result}")


def my_func2(x, y):
    x, y = float(x), int(y)
    if x <= 0 or y >= 0:
        return "Не выполненно условие ввода данных:\n x должен быть больше 0 \n y должен быть меньше 0"
    else:
        result = 1
        for _ in range(abs(y)):
            result /= x
        return f"Результат возведения x в степень y: {round(result, 4)}"


num_1 = input("Введите положительное число, x = ")
num_2 = input("Введите целое отрицательное число, y = ")

print(my_func2(num_1, num_2))