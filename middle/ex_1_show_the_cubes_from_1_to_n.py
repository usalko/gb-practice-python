import ast

print('Упражнение 1. Найти кубы чисел от 1 до N')
# Ввод и определение типа
n = ast.literal_eval(input('Введите число: '))
if not isinstance(n, int):
    print(f'Извините, не могу показать таблицу. {n} не является целым числом.')
else:
    print(f'Кубы чисел чисел от 1 до {n}')
    print('numbers: \t' + '\t'.join(map(str, range(1, n + 1))))
    print('cubes:   \t' + '\t'.join(map(lambda x: str(x**3), range(1, n + 1))))
