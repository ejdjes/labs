average = 0

file = open('C:/2к/ИПО/лабы/10/z1.txt', 'r', encoding='utf-8+')
lines = file.readlines()

for line in lines:
    line = line.replace('\n', '')
    student = line.split(' ')
    mark = int(student[2])

    if mark < 3:
        print(line)

    average += mark

file.close()
average /= len(lines)
print('Средняя оценка =', average)

