n = int(input('Введите число монеток: '))
from random import randint
a, b = 0, 0
for i in range(n):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0: a += 1
    else: b += 1
print()
if a > b:
    print(f'Нужно перевернуть {b} монеток')
else:
    print(f'Нужно перевернуть {a} монеток')