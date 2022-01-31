import ast

print('2. Даны два числа. Показать большее и меньшее число')
val1 = ast.literal_eval(input('Введите первое число: '))
val2 = ast.literal_eval(input('Введите второе число: '))
print(f'Большее число: {max(val1, val2)}')
print(f'Меньшее число: {min(val1, val2)}')
