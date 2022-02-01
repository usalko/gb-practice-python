import ast

print('8. Показать четные числа от 1 до N')
n = ast.literal_eval(input('Введите число N: '))
if not isinstance(n, int):
    print(f'Извините, не могу показать числа. {n} не является целым числом.')
elif n <= 0:
    print(f'Извините, не могу показать числа для {n}. N < 1')
else:
    print(f'Четные числа от 1 до {n}: [{", ".join([str(i) for i in range(1, n+1) if i % 2 == 0])}]')
