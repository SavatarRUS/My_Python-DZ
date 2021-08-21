dohod = float(input('Сколько сотставил ваш доход в (EUR): '))
rashod = float(input('Сколько сотставил ваш расход в (EUR): '))
profit = dohod - rashod
if dohod > rashod:
    print(f'Фирма работает прибыльно. Ваша прибыль состовляет {profit:02}EUR ')
    print(f'Рентабильность составила {100 * profit / dohod:1f}%')
    workers = int(input('Сколько сотрудников работает в вашей Фирме? '))
    print(f'Прибыль в расчете на одного сотрудника состовляет {profit/workers:02}EUR')
elif rashod == dohod:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')
