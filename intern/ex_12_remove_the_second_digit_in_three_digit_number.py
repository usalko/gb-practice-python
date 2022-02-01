import ast

print('12. Удалить вторую цифру трёхзначного числа')
value = ast.literal_eval(input('Введите трехзначное число: '))
if not isinstance(value, int):
    print(f'Извините, не могу показать цифру. {value} не является целым числом.')
elif value > 999 or value < 100:
    print(f'Извините, не могу показать цифру для {value}. Число не является трехзначным')
else:
    print(f'Двузначное число коророе получается после удаления средней цифры из трехзначного {value}: {str(value)[0] + str(value)[2]}')
