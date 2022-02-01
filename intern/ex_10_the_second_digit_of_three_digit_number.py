import ast

print('10. Показать вторую цифру трёхзначного числа')
value = ast.literal_eval(input('Введите трехзначное число: '))
if not isinstance(value, int):
    print(f'Извините, не могу показать цифру. {value} не является целым числом.')
elif value > 999 or value < 100:
    print(f'Извините, не могу показать цифру для {value}. Число не является трехзначным')
else:
    print(f'Вторая цифра для трехзначного числа {value}: {str(value)[1]}')
