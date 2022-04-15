A = []


def changeElem(index, value):
    A[index] = value


m = int(input('m ='))
for i in range(m):
    A.append(input(f'Введите {i + 1} элемент: '))

oldFirstElem = A[0]
changeElem(0, A[-1])
changeElem(-1, oldFirstElem)

print(A)