import ast

print('7. Показать числа от -N до N')
n = ast.literal_eval(input('Введите число N: '))
if not isinstance(n, int):
    print(f'Извините, не могу показать числа. {n} не является целым числом.')
elif n <= 0:
    print(f'Извините, не могу показать числа для {n}. N < 0')
else:
    print(', '.join([str(i) for i in range(-n, n+1)]))
