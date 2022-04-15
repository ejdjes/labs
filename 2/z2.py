from math import sqrt
x = float(input('Введите x: '))
y = 0
if x % 2 == 0:
    y = sqrt(x)
else:
    y = 1
print(f'y={y}')