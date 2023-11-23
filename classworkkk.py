  #toetus
grupp = input("ruhma nimetus: ")
if grupp == "TARgv23":
    puudumised = int(input("Mitu puudumist sul on?: "))
    if puudumised < 15:
        hinne = float(input("Mis on keskmine hinne?: "))
        if hinne > 3.8:
             print("Toetus!")
        else:
             print("Liiga madal keskmine hind. Toetust ei ole.")
    else:
         print("Toetus ei maaratakse.")
else:
     print("Ruhma nimetus ei sobi.") 

#kalkulaator
try:
    a = float(input("Esimene arv: "))   
    b = float(input("Teine arv: "))
    try:
        t = input("Tehe: ")
        if t in ['+', '-', '/', '*', '**', '//']:
            if t == '+':
                v = a + b
            elif t == '-':
                v = a - b
            elif t == '*':
                v = a * b
            elif t == '**':
                v = a ** b
            elif t == '/':
                if b == 0:
                    v = "DIV/0"  
                else:
                    v = a / b
            elif t == '//':
                v = a // b
            print("{0} {1} {2} = {3}".format(a, t, b, v))
        else:
            print("Tundmatu mark")
    except:
        print("Vale tehte sisend")
except ValueError:
    print("Vale arv sisend")
except ZeroDivisionError:
    print("Nulliga jagamine")

 
 
 #kolmnurk
a=float(input("Alpha:"))
b=float(input("Betta:"))
c=float(input("Gamma:"))
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
    else:
        print("Nurgad")
else:
    print("Andmed on vale")
