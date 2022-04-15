C = 0
print('Введите N')
N = int(input())
while N > 0:
    C = C + N % 10
    N = N // 10
print(f'C={C}')
