# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def user_param(name, surname, year_of_birth, city, email, tel):
    return name, surname, year_of_birth, city, email, tel


print(user_param(name=input('Ваше имя:'), surname=input('Ваша Фамилия:'), year_of_birth=input('Ваш год рождения:'),
                 city=input('Ваш город проживания:'), email=input('Ваш email:'), tel=input('Ваш телефон:')))
