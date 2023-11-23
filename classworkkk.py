#  #toetus
#grupp = input("ruhma nimetus: ")
#if grupp == "TARgv23":
#    puudumised = int(input("Mitu puudumist sul on?: "))
#    if puudumised < 15:
#        hinne = float(input("Mis on keskmine hinne?: "))
#        if hinne > 3.8:
#             print("Toetus!")
#        else:
#             print("Liiga madal keskmine hind. Toetust ei ole.")
#    else:
#         print("Toetus ei maaratakse.")
#else:
#     print("Ruhma nimetus ei sobi.") 

##kalkulaator
#try:
#    a = float(input("Esimene arv: "))   
#    b = float(input("Teine arv: "))
#    try:
#        t = input("Tehe: ")
#        if t in ['+', '-', '/', '*', '**', '//']:
#            if t == '+':
#                v = a + b
#            elif t == '-':
#                v = a - b
#            elif t == '*':
#                v = a * b
#            elif t == '**':
#                v = a ** b
#            elif t == '/':
#                if b == 0:
#                    v = "DIV/0"  
#                else:
#                    v = a / b
#            elif t == '//':
#                v = a // b
#            print("{0} {1} {2} = {3}".format(a, t, b, v))
#        else:
#            print("Tundmatu mark")
#    except:
#        print("Vale tehte sisend")
#except ValueError:
#    print("Vale arv sisend")
#except ZeroDivisionError:
#    print("Nulliga jagamine")

 
 
# #kolmnurk
#a=float(input("Alpha:"))
#b=float(input("Betta:"))
#c=float(input("Gamma:"))
#if a>0 and b>0 and c>0:
#    if a+b+c==180:
#        print("Kolmnurk")
#    else:
#        print("Nurgad")
#else:
#    print("Andmed on vale")





#1. Определить и вывести большее из двух вводимых чисел.

#2. Составить блок-схему программы подсчета суммы только отрицательных из трех данных чисел.

#3. Составить блок-схему программы радиоуправляемой машинки.

#4. Проверить правильность вводимого личного кода у N  человек. 



##1
#n1 = int(input())
#n2 = int(input())
#if n1 > n2:
#    print(f'Большее число оказалос {n1}')
#else:
#    print(f'Большее число оказалось {n2}')

##2
#count = 0
#for i in range(3):
#    a = int(input())
#    if a < 0:
#        count += a
#print(count)

#3
#a = 5
#print('Наберите направление движения для машинки, для этого используйте слова "влево, вправо, прямо, назад"')
#for i in range(a):
#    print(f'У вас осталось {a-i} движений/движение')
#    direction = input("Введите направление движения")
#    if direction = "Влево"
#        print("Вжжж, машина поворачивает налево")
#    elif direction = "Вправо":
#        print("Вжжж, машина поворачивает направо")
#    elif direction = "Прямо":
#        print("Машина разгоняется по прямой!")
#    elif direction = "Назад":
#        print("Машина сдает задним ходом.")
#    else:
#        print("Выбрано несуществующее направление движения.")

 #4


b = 4
a = 4
a = 2*a+3*b
b=a/2*b
print(b)

a = 6
b = 4
a = 2*a+3*b
b = a/2*b

print(a)