import random
import math




#for i in range(10):
#    r = float(input("Sisentage R: "))
#    if r > 0:
#        s = math.pi*(r**2)
#        print(f'S={s}')
#    else:
#        print("R peab olema > kui 0.")

#x = 0
#while x < 10:
#    r = float(input("Sisentage R: "))
#    if r > 0:
#        s = math.pi*(r**2)
#        print(f'S={s}')
#        x += 1
#    elif r < 0:
#        print("S peab olema rohkem kui 0")



##6.    С клавиатуры вводятся N чисел.

##Составьте программу, которая определяет количество отрицательных,

## количество положительных и количество нулей среди введенных чисел.  

##Значение N вводится с клавиатуры.

#n = int(input("Sisestage numbride arv: "))

#null = 0 
#pos = 0
#neg = 0

#for i in range(n):
#    n1 = int(input("Sisestage number: "))
#    if n1 > 0:
#        pos += 1
#    elif n1 == 0:
#        null += 1
#    elif n1 < 0:
#        neg += 1

#print(f'{pos} - positiivsete arvude arv ')
#print( )
#print(f'{neg} - negatiivsete arvude arv')
#print()
#print(f'{null} - nullide arv')


##7.    Вывести на экран числа, кратные К из промежутка [А,В].

#k = float(input("Sisestage jagaja"))
#print("Sisestage intervall A-st B-ni.")
#a = int(input("A: "))
#b = int(input("B: "))
#count = 0

#for i in range(a, b+1):
#    if i % k == 0:
#        print(i)
#        count += 1
#print(f'{count} numbrit.')




## 8.    Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =
## 2,5 см) для значений длин от 1 до 20 дюймов.
#print(f'1 toll võrdub 2,5 sentimeetriga.')
#for i in range(1, 21):
#    print(f'{i} tolli võrdub {i*2.5} sentimeetriga.')





##9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?

#s = float(input("Kui palju te raha soovite investeerida?: "))
#n = int(input("Kui mitmeks aaastaks soovite raha panka investeerida?: "))

#for i in range(n):
#    s = s * 1.03

#print(s)



##10. Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.

#for i in range(10):
#    a = int(input())
#    b = int(input())
#    if a > b:
#        print(a, "rohkem")
#    elif b > a:
#        print(b, "rohkem")




##11.Найти произведение двузначных нечетных чисел, кратных случайно сгенерированному числу.
#count = 1

#for i in range(1000):
#    k = random.randint(2,10)
#    if i % 2 != 0:
#        if i % k == 0:
#            print(f'{i} кратно {k}')
#            count *= i
#print(count)




##12.В бригаде, работающей на уборке сена, имеется N сенокосилок.

##Первая сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем предыдущая.

##Сколько часов проработала вся бригада?


#n = int(input("Количество сенокосилок: "))
#m = int(input("Сколько МИНУТ работала первая косиллка?: "))
#total = 0
#for i in range(n):
#    m = m + 10
#    total += m
#print(total)



##15.Написать программу, выводящую в столбик десять строк, в каждой печатая цифры от 0 до 9, то есть в таком виде:
#for i in range(10):
#    print("0 1 2 3 4 5 6 7 8 9")






##16.Напишите программу, печатающую столбик строк такого вида:
#for i in range(1,10):
#    print(("0 " * (i-1)) + str(i) + " " + ("0 " * (9-i)))




##17.Напишите программу, печатающую столбик таблицу умножения такого вида:
#n = int(input("Таблица умножения какого числа?: "))

#for i in range(1, 10):
#    print(f'{n} * {i} = {n * i}')





##18.    Даны натуральные числа от 20 до 50. Напечатать те из них, которые делятся на 3, но не делятся на 5.

#for i in range(20,51):
#    if i % 3 == 0:
#        if i % 5 != 0:
#            print(i)


##22.    Найти сумму чисел от 100 до 200, кратных 17.
#for i in range(100, 201):
#    if i % 17 == 0:
#        print(i)







##28.    Реализуйте "мини лотерею". Пусть компрьютер "задумает число", а пользователь его должен отгадать. В конце сообщив количество попыток.
#count = 0
#k = random.randint(1, 50)
#print("Я загадал число от 1 до 50! Угадай его!")
#for i in range(1,51):
#    v = int(input())
#    if v != k:
#        count += 1
#        print(f'Неверно! Попробуй еще раз! Количество неверных попыток: {count}')

#    elif v == k:
#        print(f'Правильно, {v} - верный ответ!')
#        print(f'Общее количество невеных попыток: {count}')





##29.Напишите программу, печатающую столбик строк такого вида:
#for i in range(10):
#    for y in range(10):
#        if y == 0 or i==y:
#            print("x",end=" ")
#        else:
#            print("0", end=" ")
#    print( ) 





##31.  Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.
##Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней.

#k = int(input("Кол-во котлет: "))
#m = int(input("На одну сковородку помещается: "))
#v1 = k // m
#v2 = k % m

#if v2 == 0:
#    if v1 > 5: 
#        print(f'Понадобится ровно {v1} сковородок, что бы пожарить {k} котлет.')
#    elif v1 < 5:
#        print(f'Понадобится {v1} сковородки, что бы пожарить {k} котлет.')
#else: 
#    print(f'Всего понадобится {v1} полных сковородок и на последней дожарить еще {v2}.')


a = 100
while not a <= 0:
    a = a // 2
    print(a)