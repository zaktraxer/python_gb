def recApowB(a, b):
    if b == 0:
        return 1
    return a * recApowB(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(recApowB(a, b))