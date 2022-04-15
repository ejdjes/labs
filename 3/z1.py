arr = [1, 3 , 5, 7, 9, 2, 1, 6]
sum = 0
i = 0
for i in arr:
    if i % 2 != 0:
     sum += arr[i]

while arr[i] % 2 != 0:
    sum += arr[i]
    i += 1
print('Сумма:', sum)