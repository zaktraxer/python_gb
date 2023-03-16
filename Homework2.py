number = int(input("Введите трехзначное число - "))
summa=int(((number - number%10)/10)%10 + number/100 + number%10)
print(f"Сумма цифр числа равна {summa}")
