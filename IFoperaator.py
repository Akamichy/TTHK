#1.a
#from stringprep import in_table_c8


#name = input("Mis on sinu nimi?: ")
#if name == "Juku":
#    age = int(input("Kui vana sa oled?: "))
#    if age < 6 and age > 0:
#        print('Pilet on tasuta')
#    elif age < 14 and age >= 6:
#        print("Sul on laste pilet")
#    elif age < 65 and age > 14:
#        print("Sul on tais pilet")
#    elif age > 65 and age < 100:
#        print("Pilet on soodukaga")
#    if age == 0 or age == 100:
#        print("Viga andmetega")
#else:
#    print('Vale nimi.')
##1.b

#name1 = input("Esimene nimi: ")
#name2 = input("Teine nimi: ")
#print(f'Kallid {name1} ja {name2}, tana te olete pinginaabrid!')

#a = float(input("A: "))
#b = float(input("B: "))
#s = a * b
#print(f'{s} ruutmeetrid')
#kusimus = input("Kas te soovite remonti teha? (ei voi jah): ").lower()
#if kusimus == "jah":
#    hind1 = float(input("Kui palju maksab ruutmeeter?: "))
#    hind = hind1 * s
#    print(f'{hind} on kokkuhind.')
#    if hind > 700.0:
#        print(f'Aga voime pakkuda remonditood soodukaga, kokku tuleb {round(hind*0.7)}')
#elif kusimus == "ei":
#    print("Head paeva teile!")

#kus = float(input("Mis praegu temperatuur on?: "))
#kus1 = input("Kas temperatuur on ule 18 kraadi?: ").lower()
#if kus1 == "jah":
#    print("See on soovitav toasoojus talvel.")
#else:
#    print("Liiga kulm")

#pikkus = int(input("Mis on sinu pikkus?: "))
#sugu = input("Mis on teie sugu?: (mees voi naine): ")
#if pikkus >= 180 and pikkus <= 220:
#    if sugu == "mees":
#        print("Oled pikk mees")
#    elif sugu == "naine":
#        print("Oled kindlasti pikk naine")
#elif pikkus < 180 and pikkus >= 170:
#    if sugu == "mees":
#        print("Oled keskmine mees")
#    elif sugu == "naine":
#        print("Oled keskmine naine")
#elif pikkus < 170 and pikkus > 130:
#    if sugu == "mees":
#        print("Oled luhike mees")
#    elif sugu == "naine":
#        print("Oled luhike naine")
#else:
#    print("viga andmetega")

#kokkuhind1 = 0
#kus = input("Kas te soovite piima osta?: ").lower()
#kus2 = input("Kas te soovite saia osta?: ").lower()
#kus3 = input("Kas te soovite leiba osta?: ").lower() 
#if kus == "jah":
#    kokkuhind1 += 1.20
#if kus2 == "jah":
#    kokkuhind1 += 1.27
#if kus3 == "jah":
#    kokkuhind1 += 0.80
#if kokkuhind1 == 0:
#    print("Ta lahkus tuhjade katega.")
#else:
#    print(f'Kokkuhind on {round(kokkuhind1)}.')


#a = float(input("A: "))
#b = float(input("B: "))
#if a == b: 
#    print("See on ruut")
#else:
#    print("Kahjuks see ei ole ruut")

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


#age = int(input("Palun sisestage oma vanus: "))
#if age % 10 == 0:
#    print("See on teie juubel!")
#elif age % 10 != 0:
#    print("See ei ole teie juubel.")

#for i in range(5):
#    hind = float(input("toote hind: "))
#    if hind <= 10:
#        hind = hind * 0.9
#        print(round(hind))
#    if hind > 10:
#        hind = hind* 0.8
#        print(round(hind))

#sugu = input("Mis on teie sugu?: (mees voi naine)")
#if sugu == "mees":
#    age = int(input("Mis on teie vanus?: "))
#    if age >= 16 and age <= 18:
#        print("kandideerija sobib antud meeskonda")
#    else:
#        print("kandideerija ei sobi")
#else:
#    print("kandideerija ei sobi")

inim = int(input("Kui palju inimesi?: "))
bus = int(input("Kui palju on voimalik bussi sisse tulla?: "))
count = 0 
for i in range(10000000):
    if inim > 0:
        inim -= bus
        count += 1
    elif inim <= 0:
        break
print(f'On vaja {count} bussid. ')

#count1 = 0 
#count1 = inim // bus
#print(count1)

