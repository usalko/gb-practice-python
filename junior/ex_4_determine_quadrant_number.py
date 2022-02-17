import ast

print('Упражнение 4. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0')
# Ввод и определение типа
x = ast.literal_eval(input('Введите координату X: '))
y = ast.literal_eval(input('Введите координату Y: '))
if not isinstance(x, float) and not isinstance(x, int):
    print(f'Извините, не могу определить номер четверти. {x} не является числом.')
elif not isinstance(y, float) and not isinstance(y, int):
    print(f'Извините, не могу определить номер четверти. {y} не является числом.')
elif x > 0 and y > 0:
    print(f'Точка ({x}, {y}) находится в первой четверти')
elif x < 0 and y > 0:
    print(f'Точка ({x}, {y}) находится во второй четверти')
elif x < 0 and y < 0:
    print(f'Точка ({x}, {y}) находится в третьей четверти')
elif x > 0 and y < 0:
    print(f'Точка ({x}, {y}) находится в четвертой четверти')
elif x == 0 and y == 0:
    print(f'Координата ({x}, {y}) находится в 0 точке, что противоречит условиям задачи')
else:
    raise BaseException(f'Не возможно определить номер четверти для координаты ({x}, {y})')