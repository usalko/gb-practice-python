import ast

print('11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа')
value = ast.literal_eval(input('Введите число из отрезка [10, 99]: '))
if not isinstance(value, int):
    print(f'Извините, не могу показать наибольшую цифру. {value} не является целым числом.')
elif value > 99 or value < 10:
    print(f'Извините, не могу показать наибольшую цифру для {value}. Число не принадлежит отрезку [10, 99]')
else:
    print(f'Наибольшая цифра для числа {value}: {max(str(value)[0], str(value)[1])}')
