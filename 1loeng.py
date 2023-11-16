print("Tere tulemast".center(50))
kool = input("\tMis koolis sa opid?: ").capitalize()  # str Kool
kursus = int(input("\tMis kuursusel?: "))  # int kursus
print("Tere tulemast kooli " + kool.upper() + "\nOle hea " + str(kursus) + ".kursuse opilaseks!")  # kool on KOOL
print("Tere tulemast kooli", kool.lower(), "!\nOle hea", kursus, ".kursuse opilaseks!")  # kool="tthk"
print("Tere tulemast kooli {0}!\nOle hea {1}. kuursuse opetajaks!".format(kool, kursus))  # kool="tthk"
print(type(kool))
print(type(kursus))

arv1=float(input("Arv 1: "))
arv2=float(input("Arv 2: ")) 
print("Summa {0} + {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} - {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} * {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} / {1}={2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} astmes {1} = {2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} ja {1} jääk = {2}".format(arv1,arv2,arv1+arv2))
print("Summa {0} ja {1} jagamise täis osa {2}".format(arv1,arv2,arv1+arv2))
