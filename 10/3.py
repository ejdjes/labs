import random

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж']
generic = open('generic.txt', 'w', encoding='utf-8')

for i in range(1024):
    generic.write(random.choice(alphabet))

generic.close()

generic = open('generic.txt', 'r', encoding='utf-8')

content = generic.read()
for letter in alphabet:
    print(f'Частота появления буквы {letter} равна', content.count(letter) / len(content))

generic.close()


