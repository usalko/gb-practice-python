import ast

print('Упражнение 3. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y')
for x in (True, False):
    for y in (True, False):
        if not(x and y) == (not x or not y):
            print(f'Утверждение истинно для X = {x} и Y = {y}')
        else:
            print(f'Утверждение ложно для X = {x} и Y = {y}')
