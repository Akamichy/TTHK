﻿
##s = input("Sisesta text: ")
##s_list = list(s)
##k = len(s_list)
##if s.isdigit():
##    for t in range(k):
##        num=int(s_list[t])
##        s_list.pop(t)
##        s_list.insert(t,num)


##    summa = 0
##    for e in s_list:
##       summa += e
##    print("Summa: ", summa)
    
##print(s_list)

##e = input("Element: ") 

##try:
##    if e.isalpha():
##        ind = s_list.index(e)
##    elif e.isdigit():
##        ind = s_list.index(int(e))
##    print(f'Element {e} on {indeks} positsioonil')
##except:
##    print("Element puudub")
     
##s = input("Sisestage oma sona: ").lower()
##vok = ['a', 'e' ,'u' ,'o','i']
##num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
##tuh = [' ']
##kirj = [',', '!', '"', '#', '$', '%', '&', '/', '{', '}', '(', ')', '[', ']', '=', '?', '+', '.', '*', '_', '-', ';', ':', '<', '>', '^']
##leng = len(s)
##cntv = 0
##cntnum = 0
##cntk = 0
##cntt = 0
##cntk = 0
##for i in range(leng):
##    if s[i] in vok:
##        cntv += 1
##    elif s[i] in num:
##        cntnum += 1
##    elif s[i] in tuh:
##        cntt += 1
##    elif s[i] in kirj:
##        cntk += 1
##    else:
##        cntk += 1

##print(f'Lauses on {cntv} vokaali, {cntnum} numbri, {cntk} konsonanti, {cntt} tuhid ja {cntk} kirjavahendid.')
##onoff = True
#opilased = ['Martin', 'Eva', 'Nikolas', 'Mario', 'Mario', 'Eva']
##while onoff == True:
##    names = []
##    for i in range(5):
##        n = input("Sisesta nimi: ")
##        if n not in names:
##            print(n)
##            names.append(n)
##        elif n in names:
##            print("Такое имя уже есть в списке")
##            pass
##    names.sort()
##    for i in range(5):
##        print(names[i])
##    try:
##        v = int(input("Вы хотите изменить список (не более 5 имен)? 1 - Да"))
##        if v == 1:
##            names.clear()
##            continue
##        else:
##            print("Всего хорошего")
##            onoff = False
##    except: 
##        print("Пожалуйста, введите 1 либо 2")
       

##nlist =  []
##for i in range(len(opilased)):
##    if opilased[i] not in nlist:
##        nlist.append(opilased[i])
##    else:
##        pass
##print(nlist)
##age = [18, 40, 41, 20, 19, 36, 59, 3, 10, 12]
##count22 = 0
##print(max(age))
##print(min(age))
##leng1 = len(age)
##for i in range(leng1):
##    count22 += age[i]
##apr = count22/leng1
##print(apr)

##for i in range(leng1):
##    print(age[i]*'*')


##В Эстонии почтовые индексы состоят из 5 чисел, где первое число обозначает уезд:

##    1 – Tallinn
##    2 – Narva, Narva-Jõesuu
##    3 – Kohtla-Järve
##    4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa
##    5 – Tartu linn
##    6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa
##    7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa
##    8 – Pärnumaa
##    9 – Läänemaa, Hiiumaa, Saaremaa

##Напишите программу, которая проверяет введенный индекс(количество символов, соответствие типу данных и т. д.) и отображает уезд, к которому он относится.

##Для проверки какому уезду принадлежит индекс, надо проверить первую цифру введенного значения. Для этого введеный индекс надо преобразовать в список при помощи indeks_list=list(indeks) и взять только первый элемент для проверки indeks_list[0].

##И если почтовый индеск Нарвы, Таллинна и Кохтла-Ярве, то сообщить пользователю "Оставайтесь дома!", в остальных случаях "Носите маски!".
##from numbers import *
##from string import *
##indd = input("Пожалуйста, введите ваш индекс: ")
##lennn = len(indd)
##while ((indd.isdigit() == False)):
##    indd = input("Пожалуйста, введите корректный индекс: ")
##other2 = '4567890'
##indeks = indd[0]
##ll = list(other2)

##if indeks == '1':
##    print("Таллинн, оставайтесь дома!")
##elif indeks == '2':
##    print("Нарва, оставайтесь дома!")
##elif indeks == '3':
##    print("Кохтла-Ярве, оставайтесь дома!")
##elif indeks in other2:
##    print("Носите маски!")



##5
##Напишите программу, которая меняет местами первый и последний элементы. 
##(второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. 
##В исходном списке минимум 2 элемента.
 
##str1 = input("Пожалуйста, введите ваше слово или предложение: ")

##list1 = list(str1)
##if len(list1) < 2:
##    print("В списке должно быть минимум 2 элемента")
##else:
##    str2 = int(input("Введите количество элементов, которых нужно поменять местами: "))
##    len1 = len(list1)
##    if str2 > len1//2:
##        print("Error")
##    else:
##        ind1 = 0
##        ind2 = len1
##        for i in range(str2):
##            x = list1[ind1]
##            y = list1[ind2-1]
##            list1[ind1] = y
##            list1[ind2-1] = x

##            #list1.insert(ind1, y)
##            #list1.pop(ind2-1)
##            ind1 += 1
##            ind2 -= 1

##print(str((list1)))



##6: Бесполезные числа
##Николай задумался о поиске «бесполезного» числа на основании списка.
##Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, 
##а затем делит его на длину списка и заменяет его в списке результатом деления.
##Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции.

##int111 = input("Введите произвольный список чисел через пробел: ")
##list22 = list(map(int, int111.split()))

##print(list22)

##max11 = max(list22)
##findd = list22.index(max11)
##len11 = len(list22)
##nnum = max11 // len11
##list22[findd] = nnum

##print(list22)


##7: Sorteerimine
##Требуется создать программу, которая сортирует список чисел по убыванию/возрастанию их абсолютного значения.

##nums = input("Ввод: ")
##nums = list(nums)
##nums.sort()
##print(nums)
##nums.reverse()
##print(nums)

##8: Võrdsepikkusega elemendid
##На входе имеем список строк разной длины.

#a = ['крот', 'белка', 'выхухоль']
#b = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#c = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#list1 = []
#list2 = []
#list3 = []
#a1 = 0
#b1 = 0
#c1 = 0
##Необходимо написать программу, которая вернет новый список из строк одинаковой длины. Длину итоговой строки определяем исходя из самой большой из них. Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов. Расположение элементов начального списка не менять.

##['крот____', 'белка___', 'выхухоль']
##['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
##['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

#for i in range(len(a)):
#    list1.append(len(a[i]))
#max1 = max(list1)
#for i in range(len(a)):
#    a[i] = a[i].ljust(max1, '_')


#for i in range(len(b)):
#    list2.append(len(b[b1]))
#    b1 += 1
#max2 = max(list2)
#for i in range(len(b)):
#    b[i] = b[i].ljust(max2, '_')


#for i in range(len(c)):
#    list3.append(len(c[c1]))
#    c1 += 1
#max3 = max(list3)
#for i in range(len(c)):
#    c[i] = c[i].ljust(max3, '_')

#print(a)
#print(b)
#print(c)

##9: Nimi kontroll
##Надо спросить имя человека. Проверь чтобы в имени были только буквы.
##Отобрази приветствие, используя имя с большой буквы.
##Посчитай сколько букв в имени. Найти количество гласных и согласных букв с слове.
##Выведи на экран буквы имени в алфавитном порядке.(если буква встречается несколько раз, то повторять ее не надо)
#name = input("Введите ваше имя: ")
#while name.isalpha() != True:
#    name = input("Введите ваше имя: ")
#name.capitalize()
#print(f'Здравствуйте, {name}! ')
#count = 0
#count1 = 0
#print(len(name))
#ss = "euioay"
#list33 = ""
#for i in range(len(name)):
#    if name[i] == " ":
#        continue
#    elif name[i] in ss:
#        count += 1
#    else:
#        count1 += 1
#for i in range(len(name)):
#    if name[i] in list33:
#        continue
#    else:
#        list33 += name[i]
#list33.sort()
#print(f'В имени {count} гласных и {count1} согласных.')
#print(list33)
def summa(a,b):
    pass
print(summa(4,2))