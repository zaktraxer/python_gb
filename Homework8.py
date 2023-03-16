n,m,k = int(input('Введите 1-ю сторону: ')),int(input('Введите 2-ю сторону: ')),int(input('Введите количество долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')