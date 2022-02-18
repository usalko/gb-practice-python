import ast


print('Упражнение 3. Возведите число А в натуральную степень B используя цикл')
# Ввод и определение типа
a = ast.literal_eval(input('Введите число A: '))
n = ast.literal_eval(input('Введите степень n: '))
if not isinstance(a, float) and not isinstance(a, int):
    print(f'Извините, не могу вычислить результат. {a} не является числом.')
elif not isinstance(n, int):
    print(f'Извините, не могу вычислить результат. {n} не является целым числом.')
else:
    result = 1
    for i in range(1, n + 1):
        result *= a
    print(f'Результат возведения {a} в степень {n}: {result}')
