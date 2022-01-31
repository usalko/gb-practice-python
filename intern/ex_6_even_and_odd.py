import ast

print('6. Выяснить является ли число чётным')
val = ast.literal_eval(input('Введите число: '))
if val % 2 == 0:
    print(f'Число {val} четное')
elif not isinstance(val, int):
    print(f'Извините, не могу проверить на четность число {val} которое не является целым.')
else:
    print(f'Число {val} нечетное')