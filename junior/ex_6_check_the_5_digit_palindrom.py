import ast

print('Упражнение 6. Программа проверяет пятизначное число на палиндромом.')
# Ввод и определение типа
palindrom_candidate = input('Введите пятизначное число: ')
if len(palindrom_candidate) != 5:
    print(f'Извините, не могу проверить число. Число символов не равно 5')
elif len(list(filter(lambda x: x.isnumeric(), palindrom_candidate))) != 5:
    print(f'Извините, не могу проверить число. {palindrom_candidate} в нем некоторые цифры не являются числами.')
elif palindrom_candidate == palindrom_candidate[::-1]:
    print(f'Число {palindrom_candidate} является палиндромом')
else:
    print(f'Число {palindrom_candidate} не является палиндромом')
