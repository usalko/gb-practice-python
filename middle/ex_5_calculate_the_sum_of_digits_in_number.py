import ast

print('Упражнение 5. Подсчитать сумму цифр в числе')
# Ввод и определение типа
input_value = ast.literal_eval(input('Введите число: '))
if not isinstance(input_value, int):
    print(f'Извините, не могу подсчитать сумму цифр. {input_value} не является целым числом.')
else:
    n = input_value
    s = n % 10
    while n // 10 > 0:
        s += n % 10    
        n = n // 10
    print(f'Сумма всех цифр в числе {input_value}: {s}')
