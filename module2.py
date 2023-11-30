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



#6.    С клавиатуры вводятся N чисел.

#Составьте программу, которая определяет количество отрицательных,

# количество положительных и количество нулей среди введенных чисел.  

#Значение N вводится с клавиатуры.

n = int(input("Sisestage numbride arv: "))

null = 0 
pos = 0
neg = 0

for i in range(n):
    n1 = int(input("Sisestage number: "))
    if n1 > 0:
        pos += 1
    elif n1 == 0:
        null += 1
    elif n1 < 0:
        n1 += 1

print(f'{pos} - positiivsete arvude arv ')
print( )
print(f'{neg} - negatiivsete arvude arv')
print()
print(f'{null} - nullide arv')
0