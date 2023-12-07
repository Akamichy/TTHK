
#s = input("Sisesta text: ")
#s_list = list(s)
#k = len(s_list)
#if s.isdigit():
#    for t in range(k):
#        num=int(s_list[t])
#        s_list.pop(t)
#        s_list.insert(t,num)


#    summa = 0
#    for e in s_list:
#       summa += e
#    print("Summa: ", summa)
    
#print(s_list)

#e = input("Element: ") 

#try:
#    if e.isalpha():
#        ind = s_list.index(e)
#    elif e.isdigit():
#        ind = s_list.index(int(e))
#    print(f'Element {e} on {indeks} positsioonil')
#except:
#    print("Element puudub")
     
#s = input("Sisestage oma sona: ").lower()
#vok = ['a', 'e' ,'u' ,'o','i']
#num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#tuh = [' ']
#kirj = [',', '!', '"', '#', '$', '%', '&', '/', '{', '}', '(', ')', '[', ']', '=', '?', '+', '.', '*', '_', '-', ';', ':', '<', '>', '^']
#leng = len(s)
#cntv = 0
#cntnum = 0
#cntk = 0
#cntt = 0
#cntk = 0
#for i in range(leng):
#    if s[i] in vok:
#        cntv += 1
#    elif s[i] in num:
#        cntnum += 1
#    elif s[i] in tuh:
#        cntt += 1
#    elif s[i] in kirj:
#        cntk += 1
#    else:
#        cntk += 1

#print(f'Lauses on {cntv} vokaali, {cntnum} numbri, {cntk} konsonanti, {cntt} tuhid ja {cntk} kirjavahendid.')
#onoff = True
opilased = ['Martin', 'Eva', 'Nikolas', 'Mario', 'Mario', 'Eva']
#while onoff == True:
#    names = []
#    for i in range(5):
#        n = input("Sisesta nimi: ")
#        if n not in names:
#            print(n)
#            names.append(n)
#        elif n in names:
#            print("Такое имя уже есть в списке")
#            pass
#    names.sort()
#    for i in range(5):
#        print(names[i])
#    try:
#        v = int(input("Вы хотите изменить список (не более 5 имен)? 1 - Да"))
#        if v == 1:
#            names.clear()
#            continue
#        else:
#            print("Всего хорошего")
#            onoff = False
#    except: 
#        print("Пожалуйста, введите 1 либо 2")
       

nlist =  []
for i in range(len(opilased)):
    if opilased[i] not in nlist:
        nlist.append(opilased[i])
    else:
        pass
print(nlist)
age = [18, 40, 41, 20, 19, 36, 59, 3, 10, 12]
count22 = 0
print(max(age))
print(min(age))
leng1 = len(age)
for i in range(leng1):
    count22 += age[i]
apr = count22/leng1
print(apr)

for i in range(leng1):
    print(age[i]*'*')


#В Эстонии почтовые индексы состоят из 5 чисел, где первое число обозначает уезд:

#    1 – Tallinn
#    2 – Narva, Narva-Jõesuu
#    3 – Kohtla-Järve
#    4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa
#    5 – Tartu linn
#    6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa
#    7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa
#    8 – Pärnumaa
#    9 – Läänemaa, Hiiumaa, Saaremaa

#Напишите программу, которая проверяет введенный индекс(количество символов, соответствие типу данных и т. д.) и отображает уезд, к которому он относится.

#Для проверки какому уезду принадлежит индекс, надо проверить первую цифру введенного значения. Для этого введеный индекс надо преобразовать в список при помощи indeks_list=list(indeks) и взять только первый элемент для проверки indeks_list[0].

#И если почтовый индеск Нарвы, Таллинна и Кохтла-Ярве, то сообщить пользователю "Оставайтесь дома!", в остальных случаях "Носите маски!".
import string 
onoff1 = False
indd = input("Введите индекс: ")
lennn = len(indd)
other = 4,5,6,7,8,9
other2 = '4567890'
if lennn == 5:
    indeks = indd[0]
    ll = list(other)

    if indeks == '1':
        print("Таллинн, оставайтесь дома!")
    elif indeks == '2':
        print("Нарва, оставайтесь дома!")
    elif indeks == '3':
        print("Кохтла-Ярве, оставайтесь дома!")
    elif indeks in other2:
        print("Носите маски!")
    onoff1 == True
else:
    print("Пожалуйста, введите корретный индекс!")
    
 