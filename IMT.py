#Задача 

#В программе должны выполняться ниже следующие действия:

#            вывод на экран приветствия "Tere! Olen sinu uus sober - Python!"
#            присваивание переменной nimi введённого пользователем имени
#            вывод на экран текста: nimi ", oi kui ilus nimi!" 
#            вывод на экран текста: nimi  "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "

#            если ответ равен единице:

#            присваивание переменной pikkus целого значения переменной введенной пользователем
#            присваивание переменной mass значения выражения в формате действительного числа
#            присваивание переменной indeks значения выражения mass /(0.01pikkus)2
#            вывод на экран имени, объединённого с текстом "! Sinu keha indeks on:" indeks с одним знаком после запятой
#            вывод оценки индекса массы тела в соответствии с таблицей ниже:

#                 Vastus	                                       Index
#Tervisele ohtlik alakaal	      < 16
#Alakaal	                                16 - 19
#Normaalkaal	                        19 - 25
#ulekaal	                                25 - 30
#Rasvumine	                        30 - 35
#Tugev rasvumine	                 35 - 40
#Tervisele ohtlik rasvumine      > 40

#            в противном случае (else):

#            вывод на экран текста "Kahju! See on vaga kasulik info!"
#            вывод на экран пустой строки

#вывод на экран текста "Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!"

#Обязательна проверка введенных пользователем ответов!

#  try:
#   a=float(input("A "))
#  except:
#   ValueError


print("Tere! Olen sinu us sober - Python!")

try:
    nimi = input("Palun, sisestage oma nimi: ")
except:
    ValueError
print(f'{nimi}, oi kui ilus nimi!')
try:
    v = int(input(f'{nimi}! Kas leian Sinu keha indeksi? 0-ei 1-jah => '))
except:
    ValueError
try:
    if v == 1:
        pikkus = int(input("Palun sisestage oma pikkus: "))
        mass = float(input("Palun sisestage oma mass: "))
        indeks = mass/(0.01*pikkus)**2
        print(f'{nimi}! Sinu keha indeks on: {round(indeks, 1)}')
        if indeks < 16:
            print("Tervisele ohtlik alakaal")
        elif indeks >=16 and indeks <=19:
            print("Alakaal")
        elif indeks > 19 and indeks <= 25:
            print("Normaalkaal")
        elif indeks > 25 and indeks <= 30:
            print("Ulekaal")
        elif indeks > 30 and indeks <= 35:
            print("Rasvumine")
        elif indeks > 35 and indeks <= 40:
            print("Tugev rasvumine")
        elif indeks > 40:
            print("Tervisele ohtlik rasvumine")
    elif v == 2: 
        print("Kahju! See on vaga kasulik info!")
        print(" ")
        print(f'Kohtumiseni, {nimi}! Igavesti sinu, Python!')
except:
    ValueError