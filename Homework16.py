from random import randint
a = [randint(1, 9) for i in range(int(input('Введите размер массива: ')))]
print(a)
print('Встречается', a.count(int(input('Введите искомое число: '))), 'раз')