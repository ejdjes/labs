arr = [1, 0, 3, 0, 5, 0, 7, 0]
average = 0
for num in arr:
    average += num
average = average // len(arr)
i = 0
while i < len(arr):
    if arr[i] == 0:
        arr[i] = average
    i += 1
print(arr)
