import ast

print('Упражнение 7. Найти расстояние между точками в пространстве 2D/3D')
point1_input = input('Введите координаты первой точку на плоскости x, y или в пространстве x, y, z :')
point2_input = input('Введите координаты первой точку на плоскости x, y или в пространстве x, y, z :')
point1 = [float(a.strip()) for a in point1_input.split(',')]
point2 = [float(a.strip()) for a in point2_input.split(',')]
if len(point1) != len(point2):
    print(f'Извините, не могу вычислить расстояние между точками. {point1} и {point2} размерность не совпадает.')
else:
    print(f'Евклидово расстояние между точками {point1} и {point2} = {sum([(a[0] - a[1])**2 for a in zip(point1, point2)]) ** 0.5}')
