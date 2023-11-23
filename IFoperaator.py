#1.a
name = input()
if name == "Juku":
    print('YES')
    age = int(input("Kui vana sa oled?"))
    if age < 6 and age > 0:
        print('Pilet on tasuta')
    elif age < 14 and age >= 6:
        print("Sul on laste pilet")
    elif age < 65 and age > 14:
        print("Sul on tais pilet")
    elif age > 65 and age < 100:
        print("Pilet on soodukaga")
    if age == 0 or age == 100:
        print("Viga andmetega")
else:
    print('NO')
#1.b

