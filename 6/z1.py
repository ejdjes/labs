N = int(input('Введите порядок матрицы: '))
A = []

print('Заполните матрицу')
for i in range(N):
    A.append([])
    for j in range(N):
        A[i].append(int(input(f'Строка {i} {j} элемент = ')))

K = int(input('Введите номер строки матрицы: '))
string = A[K]
diagElem = string[len(A[K]) - 1 - K]

i = 0
while i < len(A[K]):
    A[K][i] = A[K][i] / diagElem
    i += 1

print(A)
