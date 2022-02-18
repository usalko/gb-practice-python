import ast

print('Упражнение 4. Определить количество цифр в числе')
# Ввод и определение типа
input_value = ast.literal_eval(input('Введите число: '))
if not isinstance(input_value, int):
    print(f'Извините, не могу определить количество цифр в числe. {input_value} не является целым числом.')
else:
    i = 1
    n = input_value
    while n // 10 > 0:
        n = n // 10
        i += 1
    print(f'Количество цифр в числе {i}')
