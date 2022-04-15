import math

a = int(input('Введите основание: '))
b = int(input('Введите боковую сторону: '))

h = math.sqrt(b ** 2 - (a / 2) ** 2)
S = 1/2 * h * a

print('Площадь треугольника: ', round(S, 3))
if S % 2 == 0:
    print(S / 2)
else:
    print('Не делится')