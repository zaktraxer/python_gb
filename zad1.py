
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые 
# годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная 
# температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел.

# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

from random import randint
day = int(input("Введите количество дней - "))
count = 0
count_day = 0
warm_days = 0
temp = randint(-3, 3)
while count <= day:
    temp = temp + randint(-3, 3)
    if temp > 0:
        count_day += 1
    else:
        if warm_days < count_day:
            warm_days = count_day
        count_day =0 
    count +=1
    print(temp, end= ' ')
else:
    if warm_days < count_day:
        warm_days = count_day   
    #print(warm_days, end=' ')
print()
print(warm_days)