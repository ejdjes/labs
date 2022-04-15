n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('введите [',i,',',j,'] элимент')
        b.append(int(input()))

    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()