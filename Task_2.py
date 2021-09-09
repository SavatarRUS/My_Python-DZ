# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time - ((hours * 3600) + (minutes * 60))
if time < 0:
    print('Веденное значение не может быть меньше или нуля')
else:
    print(f"Время в формате чч:мм:сс  {hours:02} : {minutes:02} : {seconds:02}") #add :02