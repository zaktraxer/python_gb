from random import randint
input_set = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
print(input_set)
num = int(input('Введите искомое число: '))
input_set = set(input_set)
dif = 0
if num > max(input_set):
    print(max(input_set))
elif num < min(input_set):
    print(min(input_set))
else:
    while True:
        if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
            print(num - dif, num + dif)
            break
        elif num - dif in input_set:
            print(num - dif)
            break
        elif num + dif in input_set:
            print(num + dif)
            break
        else:
            dif += 1