import ast

print('3. По заданному номеру дня недели вывести его название')
day_number = ast.literal_eval(input('Введите номер дня недели: '))
if day_number == 1:
    print('Понедельник')
elif day_number == 2:
    print('Вторник')
elif day_number == 3:
    print('Среда')
elif day_number == 4:
    print('Четверг')
elif day_number == 5:
    print('Пятница')
elif day_number == 6:
    print('Суббота')
elif day_number == 7:
    print('Воскресенье')
else:
    print(f'Извините, число должно быть в диапазоне от 1 до 7. Вы ввели: {day_number}')
