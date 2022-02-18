import ast

print('Упражнение 0. Показать таблицу квадратов чисел от 1 до N')
# Ввод и определение типа
n = ast.literal_eval(input('Введите число: '))
if not isinstance(n, int):
    print(f'Извините, не могу показать таблицу. {n} не является целым числом.')
else:
    print(f'Таблица квадратов чисел от 1 до {n}')
    print('numbers: \t' + '\t'.join(map(str, range(1, n + 1))))
    print('squares: \t' + '\t'.join(map(lambda x: str(x**2), range(1, n + 1))))

