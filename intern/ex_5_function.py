import ast
import re
from math import *

print('Написать программу вычисления значения функции y = f(a)')
function = input('Введите функцию (пример: a**2 - 5): ')
val = ast.literal_eval(input('Введите число a: '))

def f(a):
    try:
        return eval(re.sub(r'(\W.*?|^)a(\W.*?|$)', r'\1' + f' {a} ' + r'\2', function).strip(' =\t'))
    except NameError as e:
        print(e)
        exit(-1)

print(f'Значение функции "{function}" для аргумента {val}: {f(val)}')
