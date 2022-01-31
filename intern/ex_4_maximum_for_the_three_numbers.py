import ast

print('4. Найти максимальное из трех чисел')
val1 = ast.literal_eval(input('Введите первое число: '))
val2 = ast.literal_eval(input('Введите второе число: '))
val3 = ast.literal_eval(input('Введите третье число: '))
print(f'Максимум из трех чисел {val1}, {val2}, {val3}: {max(val1, val2, val3)}')
