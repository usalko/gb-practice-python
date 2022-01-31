import ast

print('Упражнение 0. Вывести квадрат числа')
# Ввод и определение типа
input_value = ast.literal_eval(input('Введите число: '))
print(f'Результат {input_value*input_value}')
