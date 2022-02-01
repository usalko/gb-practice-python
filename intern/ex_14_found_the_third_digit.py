import ast

print('14. Найти третью цифру числа или сообщить, что её нет')
value = ast.literal_eval(input('Введите целое число: '))
if not isinstance(value, int):
    print(f'Извините, не могу найти третью цифру. {value} не является целым числом.')
elif value < 100:
    print(f'Число {value} не содержит третьей цифры.')
else:
    print(f'Третья цифра числа {value}: {str(value)[2]}')
