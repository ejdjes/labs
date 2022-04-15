arr = [
    [1, 'Дригов Борис Игнатович', 16, 'ПО-13'],
    [2, 'Лопатина Анастасия Михайловна', 21, 'ББ-41'],
    [3, 'Иванов Кирилл Ярославович', 18, 'ПО-32'],
]

dictionary = {}
for item in arr:
    dictionary.setdefault(item[0], [item[1], item[2], item[3]])

for userId in dictionary:
    user = dictionary[userId]
    name = str(user[0])
    if name.lower().startswith('иванов'):
        user[1] += 1
print(dictionary)
