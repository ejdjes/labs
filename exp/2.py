n = int(input('n: '))

for number in range(1, n + 1):
    strNum = str(number)
    count = 0

    for charKey in range(len(strNum)):
        if int(strNum[charKey]) == 0:
            continue
        if number % int(strNum[charKey]) == 0:
            count += 1

    if count == len(strNum):
        print(number)

        f = open('C:/2к/ИПО/лабы/10/z1.txt', 'r', encoding='utf-8+')
