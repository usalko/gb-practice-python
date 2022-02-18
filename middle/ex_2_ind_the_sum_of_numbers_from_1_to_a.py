import ast

def s(x):
    if x == 0:
        return 0
    return x + s(x - 1)

print('Упражнение 2. Найти сумму чисел от 1 до А')
# Ввод и определение типа
a = ast.literal_eval(input('Введите число: '))
if not isinstance(a, int):
    print(f'Извините, не могу найти сумму чисел. {a} не является целым числом.')
else:
    print(f'Сумма чисел от 1 до {a}: {s(a)} # Recursion approach')
    print(f'Сумма чисел от 1 до {a}: {int(a * (a + 1) / 2)} # Gaus approach')
