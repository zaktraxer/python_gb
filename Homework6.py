number = (input("Введите шестизначный номер билета - "))
if len(str(number))!=6:
    print("Неверный формат билета")
else:
    summa1=int(number[0])+int(number[1])+int(number[2])
    summa2=int(number[3])+int(number[4])+int(number[5])
    if summa1==summa2:
        print(f"Билет счастливый{summa1} {summa2}")
    else:
        print("Билет несчастливый")    

