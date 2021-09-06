start_km = int(input("Введите результаты пробежки первого дня в км: "))
finish_km = int(input("Введите общий желаемый результат в км: "))
result_days = 1
result_km = start_km
if start_km <= 0 or finish_km <= 0:
    print('Результат или стартовое значение не может быть ноль или меньше нуля!')
else:
    while result_km < finish_km:
        start_km = start_km + 0.1 * start_km
        result_days += 1
        result_km = result_km + start_km
    print(f"Вы достигнете требуемый результат на %.d день" % result_days)


