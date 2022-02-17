import ast

print('Упражнение 0. Дано число. Проверить кратно ли оно 7 и 23')
# Ввод и определение типа
input_value = ast.literal_eval(input('Введите число: '))
if not isinstance(input_value, int):
    print(f'Извините, не могу проверить число. {input_value} не является целым числом.')
elif input_value % 7 == 0:
    print(f'Число {input_value} кратно 7')
elif input_value % 23 == 0:
    print(f'Число {input_value} кратно 23')
else:
    print(f'Число {input_value} не кратно 23 и не кратно 7')
